import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
    build: {
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'index.html'),
                shooting: resolve(__dirname, 'AhirsShootingBattle/index.html'),
                sharkRace: resolve(__dirname, 'AhirSharkRace/index.html')
            }
        }
    }
});
