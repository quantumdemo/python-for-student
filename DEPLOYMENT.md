# Deployment Guide

This guide explains how to deploy the **Learn Python** platform for free using popular static site hosting services.

## Option 1: GitHub Pages (Recommended)

GitHub Pages is a great free option if your code is already on GitHub.

### Automatic Deployment (GitHub Actions)
We have included a GitHub Action that automatically builds and deploys your site whenever you push to the `main` branch.

1. Go to your repository on GitHub.
2. Click on **Settings** > **Pages**.
3. Under **Build and deployment** > **Source**, select **GitHub Actions**.
4. The next time you push code, it will automatically deploy!

### Manual Deployment
If you prefer to build manually:
1. Run `jupyter lite build`.
2. Push the `_output` directory and your `index.html`/`styles.css` to a branch (e.g., `gh-pages`).
3. Configure GitHub Pages to serve from that branch.

---

## Option 2: Vercel

Vercel is extremely easy to use and provides fast global delivery.

1. Install the Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the project root.
3. When prompted:
   - **Link to existing project?** No
   - **Project Name?** learn-python-platform
   - **Which directory?** `.` (The root directory)
   - **Modify Settings?** Yes
   - **Build Command:** `pip install jupyterlite-core jupyterlite-pyodide-kernel jupyter-server jupyterlab nbformat && jupyter lite build`
   - **Output Directory:** `.` (Note: Vercel will serve your `index.html`, which links to `_output`)
4. Vercel will give you a live URL!

---

## Option 3: Netlify

Netlify is another excellent free choice for static sites.

1. Log in to [Netlify](https://www.netlify.com/).
2. Click **Add new site** > **Import an existing project**.
3. Connect your GitHub/GitLab account and select the repository.
4. Set the build settings:
   - **Build command:** `pip install jupyterlite-core jupyterlite-pyodide-kernel jupyter-server jupyterlab nbformat && jupyter lite build`
   - **Publish directory:** `.`
5. Click **Deploy site**.

---

## Important Note on Paths
The landing page `index.html` expects the JupyterLite files to be in the `_output` folder. If you change the output directory in `jupyter_lite_config.json`, make sure to update the links in `index.html`.
