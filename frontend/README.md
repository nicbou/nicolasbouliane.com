This is my personal website, built with [Ursus](https://github.com/all-about-berlin/ursus). You can see it at <nicolasbouliane.com>. It's a reference implementation of an [Ursus](https://github.com/all-about-berlin/ursus) website.

# How to run

This project uses [mise](https://mise.jdx.dev/) to manage tools, dependencies, and tasks.

Run `mise site` to serve the site locally. It rebuilds on changes. Run `mise dev` to serve the site behind the Caddy proxy in Docker instead.

See `mise tasks` for a full list of available tasks.

# Deployments

Deployments are triggered by a GitHub webhook. See [`the production README`](.prod/README.md) for setup and deployment details.