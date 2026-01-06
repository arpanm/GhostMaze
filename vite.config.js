import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
    build: {
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'index.html'),
                shooting: resolve(__dirname, 'AhirsShootingBattle/index.html'),
                sharkRace: resolve(__dirname, 'AhirSharkRace/index.html'),
                snakeInARoom: resolve(__dirname, 'AhirsSnakeInARoom/index.html'),
                warZone: resolve(__dirname, 'AhirsWarZone/index.html'),
                chess: resolve(__dirname, 'AhirsChess/index.html')
            }
        }
    }
});
