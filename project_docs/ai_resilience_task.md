# AI Report Builder - Task List

## Todo
- [x] **Project Setup & Architecture**
    - [x] Initialize Next.js project
    - [x] Set up Prisma with PostgreSQL (Env config)
    - [x] Define Database Schema (User, Project, DataSource, Report, Alert)
    - [x] Configure Project-wide CSS (Design System basics)
    - [x] Implement Encryption Helper (AES-256) for DB Configs
    - [x] Implement Vercel Deployment Config (vercel.json & Build Fixes)

- [ ] **Authentication & User Management**
    - [x] Setup NextAuth.js (Credentials Provider)
    - [x] Create Login Page
    - [x] Create Middleware for Route Protection
    - [ ] create Super Admin Seeding Script
    - [/] **feature: User Management (Super Admin)**
        - [x] List Users
        - [x] Add/Edit User (Role assignment)
        - [x] Delete User

- [ ] **Project Management**
    - [x] Dashboard (List of Projects)
    - [x] Create New Project Wizard
    - [ ] Project Settings (Manage Team/RBAC)

- [ ] **Data Source Integration**
    - [x] Connection Manager UI
    - [x] Support Excel Upload (File storage + Schema Parsing)
    - [x] Support DB Connections (UI + Encryption)
    - [x] Connection Validation Service
    - [x] Data Source Details Page (Schema & Sample Queries)

- [ ] **Report Builder (Core)**
    - [x] AI Service Integration (Gemini Pro + Fallback)
    - [x] Dynamic Model Selection (Discovery + Caching)
    - [x] Interactive Builder UI (Chat + Preview)
    - [x] Visualization Configurator (Recharts)
    - [x] Report Viewer Page
    - [x] AI Insights Display

- [ ] **Alerts & Scheduling**
    - [x] Alert Configuration UI (Email, Frequency)
    - [x] Setup Alert Models
    - [x] Mock Scheduler Logic
    - [x] Share Report (Public Link Generation)
    - [x] Public Report Viewer Paged Link Handler

- [ ] **Verification & Polish**
    - [x] End-to-End Walkthrough
    - [x] Vercel "Demo Mode" Fallback (Mock Data for Read-Only Env)
    - [x] Report Deletion & Manual Query Editing
    - [x] Fix Project Overview Data Counts
    - [ ] UI Polish (Animations, Styling)

- [x] **Advanced Features**
    - [x] Data Source Editing
    - [x] AI Sample Queries (Generate + Link)
    - [x] Project & Report Sharing (User Picker + Access)
- [x] **UI Refinements & Bug Fixes**
    - [x] Fix Save Button logic in Report Builder
    - [x] Add Title & Viz Type fields to Report Builder
    - [x] Implement Project Settings (Reports Overview + Access)
    - [x] Fix Hydration Mismatch in Shared Links
    - [x] Ensure Share/Alert buttons appear after Save
