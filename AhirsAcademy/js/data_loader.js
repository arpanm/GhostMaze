export class DataLoader {
    constructor(basePath = './syllabus') {
        this.basePath = basePath;
    }

    async loadIndex() {
        try {
            // Adjust path if running from root vs inside AhirsAcademy
            // We assume this runs from AhirsAcademy/index.html usually, so ./syllabus is correct.
            // But if running from GhostMaze/index.html (rare), it might need adjustment.
            // For now, we assume relative path from the HTML file loading it.
            const response = await fetch(`${this.basePath}/syllabus_index.json`);
            if (!response.ok) throw new Error(`Failed to load index: ${response.statusText}`);
            return await response.json();
        } catch (error) {
            console.error("DataLoader Error:", error);
            return null;
        }
    }

    async loadFile(relativePath) {
        try {
            const response = await fetch(`${this.basePath}/${relativePath}`);
            if (!response.ok) throw new Error(`Failed to load file ${relativePath}: ${response.statusText}`);
            return await response.json();
        } catch (error) {
            console.error("DataLoader File Error:", error);
            return null;
        }
    }

    async loadQuestionBank() {
        try {
            const response = await fetch('./data/question_bank.json');
            if (!response.ok) throw new Error(`Failed to load question bank: ${response.statusText}`);
            return await response.json();
        } catch (error) {
            console.error("DataLoader Question Bank Error:", error);
            return null;
        }
    }
}

export const dataLoader = new DataLoader();
