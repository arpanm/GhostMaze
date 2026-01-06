import { ChessGame } from '../js/chess.js';
import { ChessAI } from '../js/ai.js';

console.log("=== Starting Ahirs Chess Automation Tests ===\n");

function assert(condition, message) {
    if (!condition) {
        console.error(`[FAIL] ${message}`);
        process.exit(1);
    } else {
        console.log(`[PASS] ${message}`);
    }
}

function testBoardSetup() {
    console.log("\nTesting Board Setup...");
    const game = new ChessGame();
    assert(game.board[0][0].type === 'r', "Black Rook at a8");
    assert(game.board[7][4].type === 'k', "White King at e1");
    assert(game.turn === 'w', "White starts");
}

function testPawnMoves() {
    console.log("\nTesting Pawn Moves...");
    const game = new ChessGame();
    // e2 -> e4
    const moves = game.getMoves(6, 4); // e2
    assert(moves.some(m => m.r === 4 && m.c === 4), "e2 can move to e4");
    assert(moves.some(m => m.r === 5 && m.c === 4), "e2 can move to e3");

    game.makeMove({ r: 6, c: 4 }, { r: 4, c: 4 }); // e4
    assert(game.board[4][4].type === 'p', "Pawn moved to e4");
    assert(game.turn === 'b', "Turn switched to Black");
}

function testKnightMoves() {
    console.log("\nTesting Knight Moves...");
    const game = new ChessGame();
    const moves = game.getMoves(7, 1); // b1 Knight
    assert(moves.some(m => m.r === 5 && m.c === 0), "Nb1 -> a3");
    assert(moves.some(m => m.r === 5 && m.c === 2), "Nb1 -> c3");
}

function testAI() {
    console.log("\nTesting AI Decision Making...");
    const game = new ChessGame();
    const ai = new ChessAI(game);

    // Test evaluation
    const initialScore = ai.evaluateBoard('w');
    assert(Math.abs(initialScore) < 5, "Initial board is balanced (mostly 0)");

    // Test Move Generation
    console.time("AI_FirstMove_Depth1");
    const bestMove = ai.getBestMove('w', 'easy');
    console.timeEnd("AI_FirstMove_Depth1");
    assert(bestMove !== null, "AI found a move");

    console.log(`AI chose move: from ${bestMove.from.r},${bestMove.from.c} to ${bestMove.to.r},${bestMove.to.c}`);
}

function runSimulation() {
    console.log("\nRunning Full Game Simulation (Random vs Easy AI)...");
    const game = new ChessGame();
    const ai = new ChessAI(game);

    let moves = 0;
    while (!game.isGameOver && moves < 100) {
        let move;
        if (game.turn === 'w') {
            // Random Mover
            const allMoves = game.getAllMoves('w');
            move = allMoves[Math.floor(Math.random() * allMoves.length)];
        } else {
            // AI
            move = ai.getBestMove('b', 'easy');
        }

        if (!move) {
            console.log("No valid moves?");
            break;
        }

        game.makeMove(move.from, move.to);
        moves++;
    }

    console.log(`Simulation ended after ${moves} moves. Result: ${game.isGameOver ? (game.winner ? game.winner + ' wins' : 'Draw') : 'Aborted (Limit)'}`);
    assert(true, "Simulation completed without crash");
}

try {
    testBoardSetup();
    testPawnMoves();
    testKnightMoves();
    testAI();
    runSimulation();
    console.log("\n=== All Tests Passed ===");
} catch (e) {
    console.error("Test Suite Crashed:", e);
    process.exit(1);
}
