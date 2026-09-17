# vipau.github.io

Vi Pau's personal homepage, meant to be reached from [vipau.dev](https://vipau.dev/).
Hosted on [Upsun](https://upsun.com/)

## Local development

The theme is a git submodule, so a plain `git clone` is not enough:

```sh
git clone --recurse-submodules https://github.com/vipau/vipau.github.io.git
# or, in an existing clone:
git submodule update --init --recursive
```

Then serve the site with [Hugo extended](https://gohugo.io/installation/) (the
theme compiles SCSS, so the standard build will not do):

```sh
hugo server -D    # http://localhost:1313, -D includes drafts
```

To reproduce what Upsun builds:

```sh
hugo --destination=public --minify
```

## Deployment

Pushing to `main` triggers an Upsun build (`.upsun/config.yaml`). After a
production deploy, the `post_deploy` hook points the `vipau.dev` apex A record
at the region gateway through the [deSEC](https://desec.io/) API, using the
`DESEC_TOKEN` environment variable. Preview environments skip that step.

Requests that do not match a file in `public/` reach `scripts/notfound.py`,
which returns Hugo's 404 page; without it Upsun answers them with a 502.

`baseURL` is fixed to the production domain. Hugo runs in the build hook, where
`PLATFORM_ROUTES` is not set yet, so a preview environment cannot know its own
URL: pages render fine there, but absolute URLs (RSS, sitemap, Open Graph)
still point at vipau.dev.
