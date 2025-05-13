# cicd-pipeline-generator Overview 

This project provides a standardized, config-driven CI/CD framework that automatically generates GitHub Actions pipelines from a JSON blueprint. It enforces best practices across teams while allowing customization for different tech stacks (Python, Java, Node.js, etc.) and deployment methods (Docker, Kubernetes, Terraform).

# Key Features : 

-Multi-Technology Support: Pre-built templates for Python, Java, Node.js, and more.

-Consistent Workflows: Enforce linting, testing, and security scans across all projects.

-Flexible Deployments: Supports Docker, Kubernetes, Terraform, and other deployment tools.

-Modular Design: Add new tools/languages without modifying core logic.

---------------------------------------------------------------------------------

# How it Works : 

Developer Config (JSON) → Generator Script → GitHub Actions Pipeline  

--------------------------------------------------------------------------------

# Steps To Use This Tool   : 

1 )  Clone repo : 

git clone https://github.com/Atul2401/cicd-pipeline-generator.git

 switch to directory : cd cicd-pipeline-generator

2)  Configure your Blueprint in json like :

    {
  "technology": "python",
  "build_steps": ["lint", "test", "security-scan"],
  "deploy_method": "docker" }

3) RUN generator Script : 

   python3 generate.py

   This creates .github/workflows/pipeline.yml. #this is your github action pipeline based on blueprint you provided 


4) commit and Push



---------------------------------------------------------------------------

# Benefit 

1) For Developer : 

-Zero CI/CD Knowledge Needed: Just edit cicd-blueprint.json.

-Consistency: All projects follow the same best practices.

-Fast Onboarding: New repos get CI/CD in minutes.

2) For DevOps :
   
-Centralized Maintenance: Update templates once, apply everywhere.

-Security: Enforce scans, tests, and approvals globally.

-Scalability: Add new tools without disrupting existing pipelines. 


-----------------------------------------------------------------------------------

# Scalability & Extensibility

# Adding New Technologies : 

1  create template : 

 mkdir -p templates/nodejs
touch templates/nodejs/eslint.yml

2 Update cicd-blueprint.json: 


  {
  "technology": "nodejs",
  "build_steps": ["lint"]
}

---------------------------------------

# Adding Deployment Methods

2.1  Add a new template:

touch templates/deployment/terraform.yml


2.2  Update config:

json
{
  "deploy_method": "terraform"
}

touch templates/deployment/terraform.yml
