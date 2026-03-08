---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
.template-note {
  margin-bottom: 20px;
  padding: 12px 16px;
  border-left: 4px solid #0366d6;
  background: #f6f8fa;
  border-radius: 6px;
}

.timeline-container {
  position: relative;
  padding-left: 20px;
  border-left: 2px solid #e1e4e8;
  margin: 8px 0 30px 8px;
}

.timeline-item {
  position: relative;
  margin-bottom: 16px;
}

.timeline-item::before {
  content: "";
  position: absolute;
  left: -27px;
  top: 5px;
  width: 12px;
  height: 12px;
  background-color: #0366d6;
  border-radius: 50%;
  border: 2px solid #fff;
}

.timeline-date {
  font-weight: 600;
  color: #0366d6;
  font-size: 0.95em;
  margin-bottom: 2px;
}

.timeline-content {
  font-size: 0.95em;
  color: #24292e;
}

.exp-card,
.paper-box,
.project-card {
  display: flex;
  gap: 16px;
  margin-bottom: 20px;
  padding: 14px;
  border: 1px solid #ececec;
  border-radius: 8px;
  background: #fff;
}

.exp-logo,
.project-thumb {
  width: 72px;
  height: 72px;
  flex: 0 0 72px;
  object-fit: contain;
}

.paper-box-image {
  flex: 0 0 32%;
  max-width: 220px;
  border-radius: 8px;
  overflow: hidden;
}

.paper-box-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.paper-box-text,
.exp-content,
.project-content {
  flex: 1;
}

.exp-header {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

.exp-role,
.project-title {
  margin: 0;
}

.exp-org,
.paper-meta,
.project-meta {
  color: #555;
  margin: 4px 0 8px;
}

.paper-title {
  font-weight: 600;
  font-size: 1.06em;
  color: #1f2d3d;
  text-decoration: none;
}

.paper-links a,
.project-links a {
  margin-right: 10px;
}

.badge {
  display: inline-block;
  margin-bottom: 8px;
  padding: 2px 8px;
  border-radius: 999px;
  background: #eef6ff;
  color: #0366d6;
  font-size: 0.78em;
  font-weight: 600;
}

@media (max-width: 768px) {
  .paper-box,
  .exp-card,
  .project-card {
    flex-direction: column;
  }

  .paper-box-image {
    max-width: 100%;
  }
}
</style>

<span class="anchor" id="about"></span>
# 👋 About

<div class="template-note">
This public version ships with neutral placeholder content only. Replace the text, links, images, and optional modules with your own information before publishing.
</div>

This template is designed for a **minimal academic or professional homepage** built with **Jekyll** and **GitHub Pages**. It keeps the original single-page structure, responsive layout, sidebar profile, and optional integrations such as Google Scholar stats, project links, and downloadable CV.

Use this section for a short self-introduction: who you are, what you work on, and what kind of collaborations or roles you are open to. Keep the first paragraph concise and visitor-focused.

<span class="anchor" id="news"></span>
# 📰 News

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-date">2026.03</div>
    <div class="timeline-content">Released a public homepage template with placeholder content and reusable academic-page sections.</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-date">2026.02</div>
    <div class="timeline-content">Added sample project cards, publication cards, and simplified onboarding instructions.</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-date">2026.01</div>
    <div class="timeline-content">Prepared optional integrations for Google Scholar stats, GitHub Pages deployment, and downloadable CV links.</div>
  </div>
</div>

<span class="anchor" id="experience"></span>
# 💼 Experience

<div class="exp-card">
  <img src="{{ '/images/building-icon.svg' | relative_url }}" class="exp-logo" alt="Organization placeholder">
  <div class="exp-content">
    <div class="exp-header">
      <h3 class="exp-role">Research Intern / Visiting Student</h3>
      <span>2025 – Present</span>
    </div>
    <div class="exp-org">Organization Name</div>
    <p class="exp-desc">Briefly describe your focus area, responsibilities, or the type of research and engineering work you contribute to.</p>
  </div>
</div>

<div class="exp-card">
  <img src="{{ '/images/building-icon.svg' | relative_url }}" class="exp-logo" alt="Company placeholder">
  <div class="exp-content">
    <div class="exp-header">
      <h3 class="exp-role">Research Engineer / Software Engineer</h3>
      <span>2023 – 2025</span>
    </div>
    <div class="exp-org">Company or Lab Name</div>
    <p class="exp-desc">Use one or two sentences to summarize the role, major systems built, or the domain you worked in.</p>
  </div>
</div>

<span class="anchor" id="education"></span>
# 🎓 Education

<div class="exp-card">
  <img src="{{ '/images/building-icon.svg' | relative_url }}" class="exp-logo" alt="University placeholder">
  <div class="exp-content">
    <div class="exp-header">
      <h3 class="exp-role">Ph.D. / M.S. in Your Field</h3>
      <span>2024 – Present</span>
    </div>
    <div class="exp-org">University Name</div>
    <p class="exp-desc">Advisor: Prof. Name. Add one line on research interests, thesis topic, or program focus.</p>
  </div>
</div>

<div class="exp-card">
  <img src="{{ '/images/building-icon.svg' | relative_url }}" class="exp-logo" alt="University placeholder">
  <div class="exp-content">
    <div class="exp-header">
      <h3 class="exp-role">B.S. in Your Field</h3>
      <span>2020 – 2024</span>
    </div>
    <div class="exp-org">University Name</div>
    <p class="exp-desc">Optionally include honors, thesis title, or a short note on coursework and projects.</p>
  </div>
</div>

<span class="anchor" id="publications"></span>
# 📝 Publications

<div class="paper-box">
  <div class="paper-box-image">
    <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Publication placeholder">
  </div>
  <div class="paper-box-text">
    <div class="badge">Conference / Journal</div>
    <a href="#" class="paper-title">Sample Paper Title: Replace with Your Publication</a>
    <div class="paper-meta">A. Author, <strong>Your Name</strong>, C. Collaborator</div>
    <div class="paper-meta"><em>Venue Name, 2026</em></div>
    <div class="paper-links">
      <a href="#">[Paper]</a>
      <a href="#">[Code]</a>
      <a href="#">[Project Page]</a>
    </div>
  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image">
    <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Publication placeholder">
  </div>
  <div class="paper-box-text">
    <div class="badge">Preprint / Workshop</div>
    <a href="#" class="paper-title">Another Example Publication Entry</a>
    <div class="paper-meta">A. Author, B. Author, <strong>Your Name</strong></div>
    <div class="paper-meta"><em>arXiv or Workshop Name, 2025</em></div>
    <div class="paper-links">
      <a href="#">[Paper]</a>
      <a href="#">[Supplementary]</a>
    </div>
  </div>
</div>

<span class="anchor" id="projects"></span>
# 🧩 Projects

<div class="project-card">
  <img src="{{ '/images/project-placeholder.svg' | relative_url }}" class="project-thumb" alt="Project placeholder">
  <div class="project-content">
    <h3 class="project-title">Project Name</h3>
    <div class="project-meta">Keywords: Vision, Systems, Robotics, ML, Graphics</div>
    <p>Describe one representative project in two or three lines: what it does, why it matters, and what your role was.</p>
    <div class="project-links">
      <a href="#">[Code]</a>
      <a href="#">[Demo]</a>
    </div>
  </div>
</div>

<div class="project-card">
  <img src="{{ '/images/project-placeholder.svg' | relative_url }}" class="project-thumb" alt="Project placeholder">
  <div class="project-content">
    <h3 class="project-title">Another Project</h3>
    <div class="project-meta">Keywords: Research, Web, Data, Infrastructure</div>
    <p>This section works well for course projects, open-source work, demos, systems prototypes, or side projects.</p>
    <div class="project-links">
      <a href="#">[Code]</a>
      <a href="#">[Project Page]</a>
    </div>
  </div>
</div>

<span class="anchor" id="awards"></span>
# 🏅 Awards

- *2025* — Sample Fellowship or Scholarship
- *2024* — Sample Best Paper / Competition / Graduation Honor
- *2023* — Sample University-Level Award

<span class="anchor" id="service"></span>
# 💬 Service

- Reviewer, Conference / Journal Name
- Teaching Assistant, Course Name
- Organizer, Workshop / Reading Group / Lab Seminar
