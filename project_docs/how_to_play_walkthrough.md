# Walkthrough - Ahir's Shark Race

I have successfully developed and integrated the third game in Ahir's tactical trilogy: **Shark Race**.

## Features Implemented

### 1. 🦈 Apex Predator Mechanics
- **Dynamic Speed**: The shark's health directly impacts its racing speed. Maintaining high HP is critical for winning.
- **Sleek Racing Form**: Redesigned the shark with a streamlined torpedo shape and dynamic tail-wave animation.
- **Vibrant Ecosystem**: 
    - **Expanded Diversity**: Added **Crabs (🦀)**, **Tortoises (🐢)**, and **Octopuses (🐙)**.
    - **Enhanced Scrolling**: Implemented robust vertical scrolling for all screens using `flex-shrink: 0` and custom `scroll-spacer` elements, ensuring full accessibility on mobile browsers with persistent UI bars.
- **Structural Integrity**: Corrected HTML nesting issues to ensure all mission overlays and buttons are properly contained and interactive.
- **Field Manual**:
- **Mission Controls**:
 Every creature now has category-coded vibrant styling for a premium visual feel.
- **Boat Combat**: Humans in motorboats will occasionally fire bullets (🌑) at the shark, requiring tactical dodging.

### 2. 🌊 Aquatic Environment & Progression
- **Territory Progression**: Conquering a sector (10,000 knots) no longer ends the game. Instead, players transition to the next **Aquatic Sector**.
- **Tiers & Sectors**: 
    - 3 Sectors per Tier. 
    - Completing Sector 3 advances the player to the next **Tier** (Level).
- **Dynamic Depths**: The ocean's color and ambiance shift dynamically:
    - **Tier 1**: Sunlit turquoise reefs.
    - **Tier 2/3**: Deeper, darker midnight zones.
- **Scaling Challenge**: Each new sector and tier increases creature speeds and predator density.

### 3. 🎨 Premium Customization
- **Shark DNA**: Players can choose their shark's color (Steel Blue, Blood Red, etc.) and logo (Lightning, Wave, Jaws) before diving into the race.
- **Mandatory Briefing**: Name input validation ensures every record is personal.

### 4. 🔗 Global Trilogy Integration
- **Cross-Game Mission Carousel**: All three games are now interconnected. Players can hop between **Ghost Maze**, **Shooting Battle**, and **Shark Race** directly from the menus.
- **Unified Aesthetic**: Consistent glassmorphism UI and "Ahir Mukherjee" branding across all titles.

## Verification Results

### 🎮 Gameplay Loop
- [x] Shark movement works across Keyboard (WASD), Joystick, and Swipe.
- [x] Health correctly decreases speed below 60% and 30% thresholds.
- [x] Eating fish restores health and awards score bonuses.
- [x] Whales and Bullets correctly reduce health.

### 📊 Persistence
- [x] Leaderboard correctly saves to `localStorage` with rank-based sorting.
- [x] **Finish Bonus Visibility**: The Game Over screen and Leaderboard now explicitly display the "Finish Bonus" column, showing exactly how many points were earned for crossing the finish line.
- [x] **Difficulty-Scaled Bonus**: Race winning bonus is now dynamically applied based on difficulty:
    - **Recreational**: 1,000 pts
    - **Pro Racer**: 2,000 pts
    - **Apex Predator**: 3,000 pts

### 📱 Responsiveness
- [x] Game UI scales across Desktop and Mobile viewports.
- [x] **Hall of Fame Fix**: Enabled horizontal scrolling for the leaderboard on mobile devices to ensure all records are viewable.
- [x] Cross-game links navigate successfully in both directions.

---
**Ahir's Shark Race** is now live and fully integrated! 🦈🌊🥇
