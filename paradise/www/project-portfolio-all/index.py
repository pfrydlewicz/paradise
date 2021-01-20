import frappe

sitemap = 1

def get_context(context):
    P = frappe.get_all("Portfolio Project", filters={'publish': 1})
    projects = []
    # need to unscramble, because above line returns list of dicts
    for p in P:
        doc = frappe.get_doc("Portfolio Project", p['name'])
        projects.append(doc)

    context.projects = sorted(projects, key=lambda x: x.project_date, reverse=True)
    context.no_cache = 1
