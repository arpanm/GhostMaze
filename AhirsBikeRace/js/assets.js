export const images = {};

const assetsToLoad = [
    { name: 'player', src: new URL('../images/player.png', import.meta.url).href },
    { name: 'background', src: new URL('../images/background.png', import.meta.url).href },
    { name: 'obstacles', src: new URL('../images/obstacles.png', import.meta.url).href },
    { name: 'car', src: new URL('../images/car.png', import.meta.url).href },
    { name: 'police', src: new URL('../images/police.png', import.meta.url).href },
    { name: 'police_car', src: new URL('../images/police.png', import.meta.url).href },
    { name: 'competitor1', src: new URL('../images/competitor1.png', import.meta.url).href },
    { name: 'competitor2', src: new URL('../images/competitor2.png', import.meta.url).href }
];

export async function loadAssets() {
    const promises = assetsToLoad.map(asset => {
        return new Promise((resolve, reject) => {
            const img = new Image();
            img.src = asset.src;
            img.onload = () => {
                console.log(`Loaded asset: ${asset.name}`);
                images[asset.name] = img;
                resolve();
            };
            img.onerror = (e) => {
                console.error(`Failed to load asset: ${asset.name} at ${asset.src}`, e);
                // Resolve anyway to prevent game hanging, but log error
                resolve();
            };
        });
    });

    await Promise.all(promises);
    console.log("All assets loaded");
}
