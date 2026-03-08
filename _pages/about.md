---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span class="anchor" id="about-me"></span>
# 👋 Welcome to my homepage!

I am a **researcher / student / engineer** building a **coding agent friendly academic homepage**. Use this section for a concise introduction: who you are, what you work on, and what kinds of collaboration, positions, or research directions you are open to.

My interests lie in **your research topics here** — for example, machine learning, systems, vision, graphics, HCI, robotics, security, or computational science. Replace this paragraph with your real focus areas, and add your own Google Scholar, project, or lab links when available.

Previously, you may want to summarize your background, degree history, lab affiliations, notable experience, or a short story about how your current work evolved. Keep this paragraph personal enough to feel real, but concise enough that visitors can scan it quickly.

I am always open to discussions and collaborations. Feel free to drop me an email!


<span class="anchor" id="news"></span>
# 📰 News

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-date">2026.03</div>
    <div class="timeline-content">Released a public version of this academic homepage template with coding-agent-friendly onboarding.</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-date">2026.02</div>
    <div class="timeline-content">Refined the homepage structure to support publications, projects, honors, services, and CV maintenance.</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-date">2026.01</div>
    <div class="timeline-content">Added reusable publication cards, hover interactions, and a collapsible selected-projects section.</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-date">2025.12</div>
    <div class="timeline-content">Prepared placeholder content for interns, students, faculty, and research engineers to adapt quickly.</div>
  </div>

  <div class="timeline-item" style="margin-top: 16px;">
    <div class="timeline-date">2025.11</div>
    <div class="timeline-content">Set up GitHub Pages and an optional Google Scholar citation workflow for future customization.</div>
  </div>
  <!-- <details class="timeline-details">
    <summary class="timeline-summary">
      <span class="summary-text">Show more history ▾</span>
    </summary>
  </details> -->
</div>

<style>
/* News Timeline Styling */
.timeline-container {
  position: relative;
  padding-left: 20px;
  border-left: 2px solid #e1e4e8;
  margin-bottom: 30px;
  margin-left: 8px;
}
.timeline-item { position: relative; margin-bottom: 16px; }
.timeline-item::before {
  content: ''; position: absolute; left: -27px; top: 5px;
  width: 12px; height: 12px; background-color: #0366d6;
  border-radius: 50%; border: 2px solid #fff;
}
.timeline-date { font-weight: 600; color: #0366d6; font-size: 0.95em; margin-bottom: 2px; }
.timeline-content { font-size: 0.95em; color: #24292e; }

/* 现代化的 Show more 按钮 */
.timeline-details summary {
  display: inline-flex; align-items: center;
  margin-left: -20px;
  padding: 6px 14px; background-color: #f6f8fa;
  border: 1px solid #e1e4e8; border-radius: 20px;
  font-size: 0.85em; font-weight: 600; color: #586069;
  cursor: pointer; transition: all 0.2s ease; list-style: none;
}
.timeline-details summary:hover { background-color: #e1e4e8; color: #24292e; }
.timeline-details summary::-webkit-details-marker { display: none; }
.timeline-details[open] summary .summary-text { content: "Show less ▴"; }

/* Global Paper Box Hover Effect */
.paper-box {
  display: flex;
  margin-bottom: 24px;
  border-radius: 8px;
  padding: 14px;
  border: 1px solid #ececec;
  background-color: #ffffff;
  transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.paper-box:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.08);
  border-color: #e2e8f0;
}
.paper-box-image {
  flex: 0 0 32%;
  margin-right: 18px;
  border-radius: 8px;
  overflow: hidden;
  position: relative;
  transform: translateZ(0);
}
.paper-box-image video, .paper-box-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.paper-box-text { flex: 1; }
.paper-box-text .title {
  font-weight: 600;
  font-size: 1.06em;
  color: #1f2d3d;
  text-decoration: none;
  transition: color 0.2s ease;
}
.paper-box-text .title:hover { color: #0366d6; }
.paper-box-text .authors { margin: 4px 0 3px 0; color: #333; font-size: 0.95em; }
.paper-box-text .venue { margin-bottom: 4px; color: #555; font-size: 0.95em; }
.paper-box-text .desc { font-size: 0.9em; margin: 6px 0 8px 0; color: #444; }
.paper-box-text .links a {
  margin-right: 10px;
  font-size: 0.9em;
  font-weight: 500;
  color: #0366d6;
  text-decoration: none;
}
.paper-box-text .links a:hover { text-decoration: underline; color: #005cc5; }
.badge {
  position: absolute; top: 6px; left: 6px;
  background: rgba(0, 0, 0, 0.72); color: #fff;
  padding: 2px 6px; border-radius: 4px; font-size: 0.75em;
  backdrop-filter: blur(4px);
}

/* Education & Experience Cards */
.exp-card {
  display: flex; align-items: flex-start;
  background: #fdfdfd; border: 1px solid #eaeaea;
  border-radius: 8px; padding: 16px; margin-bottom: 16px;
  transition: background-color 0.2s;
}
.exp-card:hover { background: #f8f9fa; }
.exp-logo {
  width: 72px;
  height: 72px;
  flex-shrink: 0;
  margin-right: 18px;
  border-radius: 4px;
  object-fit: contain;
}
.exp-content { flex-grow: 1; display: flex; flex-direction: column; justify-content: center; min-height: 72px; }
.exp-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }
.exp-role { font-weight: 600; font-size: 1.05em; color: #24292e; margin: 0; }
.exp-time { font-size: 0.9em; color: #586069; white-space: nowrap; }
.exp-org { font-weight: 500; color: #0366d6; font-size: 0.95em; margin-bottom: 6px; }
.exp-desc { font-size: 0.9em; color: #444; margin: 0; line-height: 1.5; }

/* Highlights & Collapsible */
.highlight-award { font-weight: 600; color: #b31b1b; background: #fff0f0; padding: 2px 6px; border-radius: 4px; }
.highlight-honor { font-weight: 600; color: #005cc5; background: #f0f8ff; padding: 2px 6px; border-radius: 4px; }

details.projects-section summary {
  cursor: pointer; font-weight: 600; font-size: 1.1em;
  color: #24292e; background: #f6f8fa; padding: 12px 16px;
  border-radius: 8px; border: 1px solid #eaeaea; outline: none;
  transition: background 0.2s; user-select: none;
}
details.projects-section summary:hover { background: #e1e4e8; }
details.projects-section[open] summary { margin-bottom: 20px; border-bottom-left-radius: 0; border-bottom-right-radius: 0; }
.zh-translation { font-size: 0.85em; color: #666; font-weight: normal; }
</style>

<span class="anchor" id="internships"></span>
# 💼 Internships

<div class="exp-card">
  <img src="{{ '/images/building-icon.svg' | relative_url }}" class="exp-logo" alt="Organization Placeholder">
  <div class="exp-content">
    <div class="exp-header">
      <h3 class="exp-role">Research Intern / Visiting Student</h3>
      <span class="exp-time">2025.01 - Present</span>
    </div>
    <div class="exp-org">Organization / Lab Name</div>
    <p class="exp-desc">Describe your internship or research role here. Summarize the type of work you do, the domain you contribute to, and the scope of your responsibilities.</p>
  </div>
</div>


<span class="anchor" id="education"></span>
# 🎓 Education

<div class="exp-card">
  <img src="{{ '/images/building-icon.svg' | relative_url }}" class="exp-logo" alt="University Placeholder">
  <div class="exp-content">
    <div class="exp-header">
      <h3 class="exp-role">Ph.D. / M.S. in Your Field</h3>
      <span class="exp-time">2024.09 - Present</span>
    </div>
    <div class="exp-org">University Name</div>
    <p class="exp-desc">Add one sentence on your current program, advisor, lab, or primary research direction.</p>
  </div>
</div>

<div class="exp-card">
  <img src="{{ '/images/building-icon.svg' | relative_url }}" class="exp-logo" alt="University Placeholder">
  <div class="exp-content">
    <div class="exp-header">
      <h3 class="exp-role">B.S. / B.Eng. in Your Field</h3>
      <span class="exp-time">2020.09 - 2024.06</span>
    </div>
    <div class="exp-org">University Name</div>
    <p class="exp-desc">Optionally include GPA, ranking, graduation honors, thesis title, or one short note that helps visitors understand your background.</p>
  </div>
</div>


<span class="anchor" id="publications"></span>
# 📝 Publications
<p style="font-size: 0.9em; color: #666; margin-top: -10px; margin-bottom: 20px;">
  (* Equal Contribution, † Corresponding Author)
</p>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class='badge'>Conference 2026</div>
    <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Publication Placeholder">
  </div>
  <div class='paper-box-text'>
    <a href="#" class="title">Sample Publication Title One</a>
    <div class="authors">Author A, Author B, <strong>Your Name</strong>, Author D†</div>
    <div class="venue"><em><strong>Conference / Journal Name</strong>, 2026</em></div>
    <p class="desc"><strong>TL;DR:</strong> Add one sentence that explains the core idea, result, or contribution of the paper.</p>
    <div class="links">
      <a href="#">[Paper]</a>
      <a href="#">[Code]</a>
      <a href="#">[Project Page]</a>
      <a href="#">[Dataset]</a>
    </div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class='badge'>Conference 2026</div>
    <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Publication Placeholder">
  </div>
  <div class='paper-box-text'>
    <a href="#" class="title">Sample Publication Title Two</a>
    <div class="authors">Author A, Author B, <strong>Your Name</strong>, Author D†</div>
    <div class="venue"><em><strong>Conference / Journal Name</strong>, 2026</em></div>
    <p class="desc"><strong>TL;DR:</strong> Use this card for another representative paper or preprint you want to highlight.</p>
    <div class="links">
      <a href="#">[Paper]</a>
      <a href="#">[Code]</a>
      <a href="#">[Project Page]</a>
    </div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class='badge'>Workshop / arXiv</div>
    <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Publication Placeholder">
  </div>
  <div class='paper-box-text'>
    <a href="#" class="title">Sample Publication Title Three</a>
    <div class="authors">Author A*, Author B*, <strong>Your Name</strong>, Author D†</div>
    <div class="venue"><em><strong>Workshop / arXiv</strong>, 2025</em></div>
    <p class="desc"><strong>TL;DR:</strong> Add a compact summary sentence that is easy to scan from the homepage.</p>
    <div class="links">
      <a href="#">[Paper]</a>
      <a href="#">[Code]</a>
      <a href="#">[Project Page]</a>
      <a href="#">[Demo]</a>
    </div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class='badge'>Under Review</div>
    <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Publication Placeholder">
  </div>
  <div class='paper-box-text'>
    <a href="#" class="title">Sample Publication Title Four</a>
    <div class="authors">Author A, Author B, <strong>Your Name*</strong>, Author D†</div>
    <div class="venue"><em><strong>Under Review</strong></em></div>
    <p class="desc"><strong>TL;DR:</strong> This slot works well for a recent submission, preprint, or work-in-progress project.</p>
    <div class="links">
      <a href="#">[Paper]</a>
      <a href="#">[Code]</a>
      <a href="#">[Project Page]</a>
    </div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div class='badge'>Conference 2025</div>
    <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Publication Placeholder">
  </div>
  <div class='paper-box-text'>
    <a href="#" class="title">Sample Publication Title Five</a>
    <div class="authors">Author A*, Author B*, <strong>Your Name*</strong>, Author D†</div>
    <div class="venue">
      <em><strong>Proceedings of Conference Name</strong>, 2025 (Poster)</em><br>
      <strong style="color: #b31b1b;">🏆 Optional Highlighted Award or Distinction</strong>
    </div>
    <p class="desc"><strong>TL;DR:</strong> Keep the most visible publication cards concise and easy to edit after forking.</p>
    <div class="links">
      <a href="#">[Paper]</a>
      <a href="#">[Code]</a>
      <a href="#">[Project Page]</a>
      <a href="#">[Demo]</a>
    </div>
  </div>
</div>

<span class="anchor" id="projects"></span>
# 💻 Projects

<details class="projects-section">
  <summary>📂 Click to expand selected projects</summary>

  <div class='paper-box' style="margin-top: 10px;">
    <div class='paper-box-image'>
      <div class='badge'>Systems</div>
      <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Project Placeholder">
    </div>
    <div class='paper-box-text'>
      <a href="#" class="title">Selected Project One</a>
      <div class="authors"><strong>Your Name (Lead / Owner)</strong>, Collaborator A, Collaborator B</div>
      <div class="venue"><em>Tags: Systems, Infrastructure, Engineering</em></div>
      <p class="desc">Use this expandable area for selected projects that deserve more space than the main publication list. Keep title, teammates, tags, and one compact summary.</p>
      <div class="links">
        <a href="#">[Code]</a>
      </div>
    </div>
  </div>

  <div class='paper-box'>
    <div class='paper-box-image'>
      <div class='badge'>ML</div>
      <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Project Placeholder">
    </div>
    <div class='paper-box-text'>
      <a href="#" class="title">Selected Project Two</a>
      <div class="authors"><strong>Your Name</strong>, Collaborator A, Collaborator B, Collaborator C</div>
      <div class="venue"><em>Tags: Machine Learning, Vision, Data</em></div>
      <p class="desc">This slot works well for project pages, systems prototypes, open-source work, demos, or large course projects.</p>
      <div class="links">
        <a href="#">[Code]</a>
        <a href="#">[Project Page]</a>
      </div>
    </div>
  </div>

  <div class='paper-box'>
    <div class='paper-box-image'>
      <div class='badge'>Creative</div>
      <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Project Placeholder">
    </div>
    <div class='paper-box-text'>
      <a href="#" class="title">Selected Project Three</a>
      <div class="authors"><strong>Your Name</strong>, Collaborator A, et al.</div>
      <div class="venue"><em>Tags: Visualization, Design, Interactive Media</em></div>
      <p class="desc">You can also use this pattern for interdisciplinary, creative, or community-facing projects with richer descriptions.</p>
      <div class="links">
        <a href="#">[Project Page]</a>
        <a href="#">[News]</a>
      </div>
    </div>
  </div>

  <div class='paper-box'>
    <div class='paper-box-image'>
      <div class='badge'>Game / Demo</div>
      <img src="{{ '/images/project-placeholder.svg' | relative_url }}" alt="Project Placeholder">
    </div>
    <div class='paper-box-text'>
      <a href="#" class="title">Selected Project Four</a>
      <div class="authors"><strong>Your Name</strong>, Collaborator A, Collaborator B</div>
      <div class="venue"><em>Tags: Python, Demo, Product Prototype</em></div>
      <p class="desc">This final slot can hold a side project, interactive demo, engineering showcase, or anything that benefits from the collapsible project gallery.</p>
      <div class="links">
        <a href="#">[Code]</a>
      </div>
    </div>
  </div>
</details>


<span class="anchor" id="honors-awards"></span>
# 🏆 Honors and Awards

- *2025.06*, <span class="highlight-honor">Outstanding Graduate</span> <span class="zh-translation">（replace with your honor）</span> & **Outstanding Thesis Award** <span class="zh-translation">（optional translation）</span>, University Name.
- *2024.09*, Fellowship / Scholarship Name, University Name.
- *2023.09*, <span class="highlight-award">Major National / Regional Award</span> <span class="zh-translation">（optional translation）</span>, Awarding Organization.
- *2023.08*, Competition Prize or Engineering Award, Event Name.
- *2023.11*, Creative / Exhibition / Demo Award, Event Name.
- *2023.09*, Media / Video / Design Award, Institution Name.
- *2023.06*, Mathematical Modeling / Hackathon / Research Competition Award.


<span class="anchor" id="services"></span>
# 💬 Services

- *2024.09 - 2025.01*, Teaching Assistant, Course Name, University Name.
- *2024.03 - 2024.06*, Reviewer / Organizer / Mentor, Program or Workshop Name.
- *2023.09 - 2024.01*, Volunteer Service / Reading Group / Lab Support, Organization Name.
