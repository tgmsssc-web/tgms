Telangana Model Schools — Central Website Project

Project Goal

Develop and maintain websites for 193 Telangana Model Schools using one reusable website template and a centrally managed codebase.

Existing Reference Website

- School: TG Model School & Junior College, Lingapur
- Repository: https://github.com/tgmsssc-web/tgms
- Live Website: https://tgmslingapur.in

Project Principles

- Preserve the existing Lingapur website.
- Develop and test changes on the "multi-school-template" branch.
- Reuse common HTML, CSS, navigation and page layouts.
- Maintain separate information for each school.
- Use responsive, mobile-friendly designs.
- Publish only verified school information.
- Restrict publishing access to authorized administrators.

Planned Repository Structure

- "template/" — reusable school website pages
- "assets/css/" — shared stylesheets
- "assets/js/" — shared JavaScript
- "assets/images/" — common design assets
- "schools-data/" — individual school configuration files
- "scripts/" — website generation and validation tools
- "dist/" — generated website output

Common Website Pages

- Home
- About the School
- Academics
- Activities
- Examinations
- Faculty
- Gallery
- Notices
- Contact

School-Specific Information

Each school configuration may contain:

- Official school name and school code
- District, mandal and address
- Principal and staff directory
- School contact information
- Campus photographs and logo
- Academic information and notices
- Approved map location and website links

Implementation Plan

1. Inspect and document the existing Lingapur website.
2. Develop a reusable master template.
3. Separate school data from website design.
4. Test the template with five pilot schools.
5. Validate all pages, links and mobile layouts.
6. Generate and publish the remaining school websites in batches.
7. Establish centralized maintenance and backups.

Hosting and Governance

- Evaluate GitHub Pages for static website hosting.
- Select an approved central domain and school URL structure.
- Verify official school information before publication.
- Obtain required authorization for government branding and photographs.
- Never store passwords, API keys or private credentials in public repositories.

Current Status

- Existing Lingapur website is operational.
- Development branch "multi-school-template" has been created.
- Master template development is planned.
- No changes to the live website are authorized through this README alone.
