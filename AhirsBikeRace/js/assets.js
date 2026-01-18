export const images = {};

const assetsToLoad = [
    { name: 'player', src: 'images/player.png' },
    { name: 'background', src: 'images/background.png' },
    { name: 'obstacles', src: 'images/obstacles.png' },
    { name: 'car', src: 'images/car.png' },
    { name: 'police', src: 'images/police.png' },
    { name: 'police_car', src: 'images/police.png' },
    { name: 'competitor1', src: 'images/competitor1.png' },
    { name: 'competitor2', src: 'images/competitor2.png' }
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
