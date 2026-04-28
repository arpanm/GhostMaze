// Story data for 30 levels across 6 chapters
export const CHAPTERS = [
    { name: 'Operation Green Dawn', terrain: 'jungle', color: '#2d5a1e' },
    { name: 'Desert Storm', terrain: 'desert', color: '#c2a645' },
    { name: 'Deep Blue', terrain: 'underwater', color: '#1a4a6a' },
    { name: 'Frozen Wasteland', terrain: 'arctic', color: '#8ab0c0' },
    { name: 'Urban Assault', terrain: 'urban', color: '#555555' },
    { name: 'The Final Inferno', terrain: 'volcano', color: '#4a1a0a' }
];

export const STORY = {
    opening: `Commander, welcome to the Green Force.\n\nA powerful ancient artifact — the Emerald Core — has been stolen by the Scarred Red Legion. Their leader, a shadowy figure known only as "The Scar," has weaponized it to build an army of enhanced soldiers.\n\nYour mission: Lead your 8-member elite squad across 30 deadly zones to recover the Emerald Core before the Red Legion activates its full power.\n\nGear up. Name your squad. The world is counting on you.`,

    ending: `The volcano crumbles around you as you hold the Emerald Core.\n\nThe Scar removes his mask — revealing Commander Veer, your former mentor who disappeared 5 years ago. "I took it to protect everyone," he whispers. "But it... changed me."\n\nThe Core pulses with green light, healing his scars. With the artifact recovered and Veer redeemed, the Green Force stands victorious.\n\n"You did well, Commander," Veer says with a smile. "Better than I ever could."\n\nThe world is safe. For now.\n\n🏆 CONGRATULATIONS — ALL 30 LEVELS COMPLETE!`,

    chapters: [
        // Chapter 1: Jungle (Levels 1-5)
        {
            intro: "Intel reports Red Legion forces hiding in the dense Razorleaf Jungle. This is where the trail begins. Watch out for ambushes in the undergrowth.",
            levels: [
                { title: "First Contact", brief: "Clear the jungle outpost. Learn the basics of combat.", after: null },
                { title: "Ambush Alley", brief: "The enemy knows we're here. Push through the ambush zone.", after: null },
                { title: "River Crossing", brief: "Cross the dangerous river while under fire from both banks.", after: null },
                { title: "Hidden Camp", brief: "Locate and destroy the Red Legion's hidden supply camp.", after: null },
                { title: "Jungle Boss: Commander Fang", brief: "Commander Fang guards the jungle exit. Defeat him and his elite squad to proceed.", after: "Fang falls. In his pocket — a map pointing to the Scorching Desert. The Emerald Core was here, but they moved it. The chase continues." }
            ]
        },
        // Chapter 2: Desert (Levels 6-10)
        {
            intro: "The trail leads to the Burning Sands. Sandstorms reduce visibility. The Red Legion has fortified an old fortress here.",
            levels: [
                { title: "Sandstorm Entry", brief: "Navigate through blinding sandstorms to reach the fortress.", after: null },
                { title: "Oasis Trap", brief: "The oasis looks safe — it's not. Clear the trap.", after: null },
                { title: "Fortress Walls", brief: "Breach the outer walls of the Red Fortress.", after: null },
                { title: "Underground Tunnels", brief: "Fight through the tunnels beneath the fortress.", after: null },
                { title: "Desert Boss: General Blaze", brief: "General Blaze commands from the fortress core. Take him down.", after: "Blaze's comm device reveals underwater coordinates. The Emerald Core is being transported by submarine. We need to go deep." }
            ]
        },
        // Chapter 3: Underwater (Levels 11-15)
        {
            intro: "We've tracked the submarine to the Abyssal Trench. The environment is hostile — low visibility, pressure hazards. Use submarine mode wisely.",
            levels: [
                { title: "Dive Down", brief: "Descend into the ocean depths. Watch your oxygen.", after: null },
                { title: "Coral Maze", brief: "Navigate the treacherous coral formations while fighting aquatic enemies.", after: null },
                { title: "Shipwreck Ambush", brief: "The old shipwreck is crawling with Red Legion divers.", after: null },
                { title: "Submarine Chase", brief: "Board the enemy submarine and fight through its corridors.", after: null },
                { title: "Deep Boss: Admiral Depth", brief: "Admiral Depth awaits in the submarine's command center.", after: "The submarine's navigation logs reveal the Emerald Core was airlifted to an arctic research station. Bundle up, team." }
            ]
        },
        // Chapter 4: Arctic (Levels 16-20)
        {
            intro: "The frozen wasteland. Temperature drops, ice makes movement treacherous. The Red Legion has a research facility here experimenting with the Emerald Core's energy.",
            levels: [
                { title: "Frozen Landing", brief: "Establish a foothold on the icy tundra.", after: null },
                { title: "Blizzard Run", brief: "Push through the blizzard to reach the facility.", after: null },
                { title: "Ice Caves", brief: "The caves are beautiful — and deadly. Clear them.", after: null },
                { title: "Research Lab", brief: "Infiltrate the research facility. Destroy their experiments.", after: null },
                { title: "Arctic Boss: Dr. Frost", brief: "Dr. Frost has enhanced herself with Core energy. She's dangerous.", after: "Dr. Frost's research notes mention a 'final assembly' in Metro City. The Red Legion is building something big. We must stop them." }
            ]
        },
        // Chapter 5: Urban (Levels 21-25)
        {
            intro: "Metro City. Civilians evacuated. The Red Legion controls the streets. Building-to-building combat. Stay sharp, use cars to move fast.",
            levels: [
                { title: "Street Fight", brief: "Take back the main avenue from Red Legion patrols.", after: null },
                { title: "Rooftop Run", brief: "Use the rooftops to flank enemy positions below.", after: null },
                { title: "Shopping Mall Siege", brief: "The Red Legion is using the mall as a fortress. Breach it.", after: null },
                { title: "Bridge Battle", brief: "Secure the bridge — it's the only way to the city center.", after: null },
                { title: "Urban Boss: Warlord Steel", brief: "Warlord Steel commands from City Hall with heavy armor.", after: "Steel's dying words: 'The Scar waits for you in the volcano. You don't know who he really is.' Time for the final mission." }
            ]
        },
        // Chapter 6: Volcano (Levels 26-30)
        {
            intro: "Mount Inferno. The Red Legion's final stronghold built inside an active volcano. The Emerald Core is here. This ends now.",
            levels: [
                { title: "Lava Fields", brief: "Navigate the deadly lava flows to reach the volcano base.", after: null },
                { title: "Magma Tunnels", brief: "The heat is unbearable. Fight through the magma tunnels.", after: null },
                { title: "The Crucible", brief: "A massive chamber where the Red Legion forges their weapons.", after: null },
                { title: "Core Chamber", brief: "The Emerald Core is visible — but heavily guarded.", after: null },
                { title: "FINAL BOSS: The Scar", brief: "The Scar awaits. He is Commander Veer — your former mentor. End this.", after: null }
            ]
        }
    ]
};

export function getLevelData(levelIndex) {
    const chapterIndex = Math.floor(levelIndex / 5);
    const levelInChapter = levelIndex % 5;
    const chapter = STORY.chapters[chapterIndex];
    const chapterMeta = CHAPTERS[chapterIndex];
    const level = chapter.levels[levelInChapter];
    const isBoss = levelInChapter === 4;
    const diffMultiplier = 1.0 + (levelIndex / 30) * 2.0; // 1.0 to 3.0

    return {
        levelIndex,
        chapterIndex,
        levelInChapter,
        chapterName: chapterMeta.name,
        terrain: chapterMeta.terrain,
        terrainColor: chapterMeta.color,
        title: level.title,
        brief: level.brief,
        storyAfter: level.after,
        chapterIntro: levelInChapter === 0 ? chapter.intro : null,
        isBoss,
        enemyCount: 8 + Math.floor(levelIndex * 0.5),
        diffMultiplier,
        isFirstLevel: levelIndex === 0,
        isFinalLevel: levelIndex === 29
    };
}
