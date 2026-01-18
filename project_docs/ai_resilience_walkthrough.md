# AI Report Builder - Verification & Setup Guide

## Prerequisites
- Node.js installed
- Gemini API Key

## Setup Instructions

### 1. Environment Configuration
Create a `.env` file in the root directory:
```bash
cp .env.example .env
```
Update variables:
- `GEMINI_API_KEY`
- `NEXTAUTH_SECRET`
- `ENCRYPTION_KEY` (32 chars)
- *Note: `DATABASE_URL` is pre-configured for SQLite (`file:./dev.db`)*

### 2. Database Initialization
```bash
npx prisma db push
npx prisma db seed
```

### 3. Running the Application
```bash
npm run dev
```

## Verification Steps

### Phase 2: Auth & User Management (Confirmed)
1. Login as `admin@example.com` / `password123`.
2. Verify Dashboard access and Admin User Management.

### Phase 3: Data Source Integration & Report Builder
1. **Create Project**: Go to Dashboard > New Project. Create "Sales Analytics".
2. **Add Data Source**: 
   - Open Project > Data Sources > Add Source.
   - Choose **Excel**. Upload any small `.csv` or `.xlsx` (or just click next to use mock schema).
   - Alternatively, add a mock Postgres connection (Enter any details, it simulates connection).
3. **Generate Report**:
   - Go to Reports > New Report.
   - Type prompt: *"Show me the distribution of users by role"* (or any prompt).
   - Verify: AI generates a Chart (Pie/Bar) and Insight.
   - Click **Save Report**.
### Advanced Features
- **Data Source Editing**: Name and configuration can now be edited directly within the data source details page.
- **AI-Powered Sample Queries**: Use the "Generate AI Queries" button on a data source to get 5 distinct analytical questions based on your schema.
- **Clickable Sample Queries**: Clicking any sample query takes you directly to the Report Builder with the prompt pre-filled, streamlining report generation.
- **Granular Sharing**: 
    - **Projects**: Share an entire project and its reports with any user by email.
    - **Reports**: Share a specific report with a user without giving them access to the whole project.
    - **Access Control**: Choose between "View Only" and "Editor" roles for collaborators.
- **Project Settings**:
    - New Settings tab providing a centralized view of all reports.
    - Displays active **Email Alerts** and **Shared User Access** for each report.

- **AI Resilience Layer**: 
    - Implemented an **Ultra-Resilient Retry Loop** that cycles through up to **8 alternative models**.
    - Added **Exponential Backoff Delays** between attempts to respect "Requests Per Minute" quotas.
    - Verified cross-model exclusion to ensure zero duplication during fallback.
- **Enhanced Report Builder**: Added explicit fields for **Report Title** and **Visualization Type**. Save button logic and post-save navigation were also improved to ensure immediate access to sharing/alerts.
- **Hydration Fix**: Resolved SSR hydration mismatches in shared report links using a client-side date formatter.
- **Prisma Validation**: Fixed a complex relation filtering issue in `getProjects` by splitting the query logic.
- **Project Overview Stats**: Restored dynamic data counts and fixed missing imports in the overview page.
- **Report Loader**: Wrapped Report Builder in Suspense to handle search parameters during SSR.
4. **View Report**:
   - Redirects to Report List.
   - Click the Report to view details.

### Phase 4: Share & Alerts
1. **Alerts**:
   - In Report Viewer, click "Alerts".
   - Enter email and Frequency. Click "Create Alert".
2. **Public Share**:
   - Click "Share".
   - Click "Copy Public Link".
   - Open Incognito Window.
   - Paste link. Verify you can see the report **without login**.
