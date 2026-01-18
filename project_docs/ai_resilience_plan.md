# Implementation Plan - AI Report Builder

# Goal Description
Build a comprehensive Report Builder application that allows users to connect to various data sources (Databases, Excel), generate reports via AI prompts with visualizations, and schedule AI-driven insights via email alerts. The app will feature robust user management and role-based access control.

## User Review Required
> [!IMPORTANT]
> **AI Integration**: We will use **Google Gemini Pro** via the official API. The system will implement a **Smart Model Fallback** mechanism:
> 1. Check available models and daily limits.
> 2. Cache model status.
> 3. Fallback to the next best model if limits are reached.
> *Note: API Key must be provided via `GEMINI_API_KEY` environment variable.*

> [!IMPORTANT]
> **Database & Deployment**:
> - **Production (Vercel)**: We will use **PostgreSQL** (e.g., Vercel Postgres or Neon) as SQLite is not suitable for serverless writes.
> - **Configuration**: Database connection strings for *user projects* will be **encrypted at rest** using AES-256.
> - **Environments**: Support for distinct `.env.local`, `.env.development`, `.env.production` files.

> [!NOTE]
> **Reporting & Visualization**:
> - Library: **Recharts** (Standard, reliable, highly customizable React charts).
> - **Excel**: We will implement a parser to extract column names and data types upon upload to allow for schema-aware querying.
> - **Interactive Builder**: The builder will feature a chat-like interface with query preview and visualization selectors.

## Proposed Changes

### Core Infrastructure
- **Tech Stack**: Next.js 14+ (App Router), TypeScript, React.
- **ORM**: Prisma (PostgreSQL).
- **Auth**: NextAuth.js (Credentials Provider).
- **Security**: AES-256 encryption helper for DB credentials.
- **AI**: Google Generative AI SDK (`@google/generative-ai`).
- **Charts**: Recharts.

### Database Schema (Prisma)
#### [NEW] [schema.prisma](file:///Users/arpan1.mukherjee/code/AIReportBuilder/prisma/schema.prisma)
```prisma
model User {
  id        String   @id @default(uuid())
  email     String   @unique
  name      String?
  password  String   // Hashed
  role      String   // SUPER_ADMIN, USER
  projects  ProjectUser[]
  createdProject Project[] @relation("CreatedProjects")
  reports   Report[]
}

model Project {
  id          String   @id @default(uuid())
  name        String
  description String?
  ownerId     String
  owner       User     @relation("CreatedProjects", fields: [ownerId], references: [id])
  users       ProjectUser[]
  dataSources DataSource[]
  reports     Report[]
}

model ProjectUser {
  id        String @id @default(uuid())
  projectId String
  userId    String
  role      String // VIEW_ONLY, EDITOR, ADMIN
  project   Project @relation(fields: [projectId], references: [id])
  user      User    @relation(fields: [userId], references: [id])
}

model DataSource {
  id        String @id @default(uuid())
  projectId String
  type      String // BIGQUERY, MYSQL, POSTGRES, EXCEL
  encryptedConfig String // Encrypted connection string or file path
  schema    String // JSON string: { tables: [{ name, columns: [{ name, type }] }] }
  name      String
  project   Project @relation(fields: [projectId], references: [id])
}

model Report {
  id          String   @id @default(uuid())
  projectId   String
  title       String
  prompt      String
  query       String?
  vizType     String   // TABLE, BAR, LINE, PIE
  vizConfig   String?  // JSON for chart data/config
  aiInsight   String?
  createdAt   DateTime @default(now())
  project     Project @relation(fields: [projectId], references: [id])
  alerts      Alert[]
  creatorId   String
  creator     User     @relation(fields: [creatorId], references: [id])
  shareToken  String?  // Unique token for public/shared access
}

model Alert {
  id        String   @id @default(uuid())
  reportId  String
  email     String
  frequency String   // DAILY, HOURLY, WEEKLY
  report    Report   @relation(fields: [reportId], references: [id])
}
```

### Phase 1: Foundation & Auth
- **Setup**: Install `prisma`, `next-auth`, `bcryptjs`, `recharts`.
- **Auth**: Implement `app/api/auth/[...nextauth]/route.ts`.
- **Login**: `app/login/page.tsx` with premium design.

### Phase 2: User & Project Management
- **Admin**: `app/admin/users/page.tsx` for Super Admin management.
- **Dashboard**: `app/dashboard/page.tsx` listing projects.
- **Project Create**: `app/projects/new/page.tsx`.

### Phase 3: Reporting Engine & AI
- **Data Source**: `app/projects/[id]/data-sources` - Add DB/Excel with Schema Parsing.
- **AI Service**: `lib/ai.ts` - Singleton for Gemini with Model Fallback/Caching.
- **Builder**: `app/projects/[id]/reports/new` - Interactive Chat + Preview.
- **Viewer**: `app/reports/[id]/page.tsx` - Final view + Share Modal.

### Phase 4: Alerts & Production Readiness
- **Alerts**: Scheduler simulation (or Vercel Cron) for email dispatch.
- **Deployment**: Vercel configuration (`vercel.json`), Config validation.


## Implementation Plan: UI Refinements & Bug Fixes

### 1. Report Builder Enhancements
#### [MODIFY] [ReportBuilderClient.tsx](file:///Users/arpan1.mukherjee/code/AIReportBuilder/src/app/dashboard/projects/[id]/reports/new/ReportBuilderClient.tsx)
- **Save Button**: Fix logic to ensure "Save Report" button appears after regeneration.
- **Title Field**: Add explicit input for "Report Title".
- **Viz Type**: Add dropdown to manually select visualization type.
- **Post-Save buttons**: Redirect to the report viewer page after saving, which contains Share and Alert buttons.

### 2. Project Settings tab
#### [NEW] [page.tsx](file:///Users/arpan1.mukherjee/code/AIReportBuilder/src/app/dashboard/projects/[id]/settings/page.tsx)
- Create a comprehensive settings page.
- List all reports and for each:
    - Display alert configurations (User + Frequency).
    - Display user access (Shared users + Roles).

### 3. Hydration Fix
#### [MODIFY] [PublicReportViewer.tsx](file:///Users/arpan1.mukherjee/code/AIReportBuilder/src/app/share/[token]/PublicReportViewer.tsx)
- Wrap date formatting in a Client-only component or use `useEffect` to avoid SSR mismatch.
#### [MODIFY] [reports/page.tsx](file:///Users/arpan1.mukherjee/code/AIReportBuilder/src/app/dashboard/projects/[id]/reports/page.tsx)
- Apply same fix for report creation date display.

## Verification Plan
- **Save Flow**: Generate -> Edit Query -> Regenerate -> Verify Save button is visible -> Save -> Verify redirect to viewer.
- **Settings**: Visit `/settings` -> Verify reports list with alert/access info.
- **Hydration**: Open public share link -> Verify no hydration mismatch in console.
