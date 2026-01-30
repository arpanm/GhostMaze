import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
    build: {
        rollupOptions: {
            input: {
                index: resolve(__dirname, 'index.html'),
                main: resolve(__dirname, 'AhirsGhostMaze/index.html'),
                ghostMaze: resolve(__dirname, 'AhirsGhostMaze/index.html'),
                shooting: resolve(__dirname, 'AhirsShootingBattle/index.html'),
                sharkRace: resolve(__dirname, 'AhirSharkRace/index.html'),
                snakeInARoom: resolve(__dirname, 'AhirsSnakeInARoom/index.html'),
                warZone: resolve(__dirname, 'AhirsWarZone/index.html'),
                chess: resolve(__dirname, 'AhirsChess/index.html'),
                snakeAndLadder: resolve(__dirname, 'AhirsSnakeAndLadder/index.html'),
                bikeRace: resolve(__dirname, 'AhirsBikeRace/index.html'),
                academy: resolve(__dirname, 'AhirsAcademy/index.html')
            }
        }
    }
});
