import json
import yaml  # install with: pip install pyyaml
from pathlib import Path

def generate_pipeline():
    # Load JSON config
    with open("cicd-blueprint.json") as f:
        config = json.load(f)
    
    # Create .github/workflows directory if missing
    workflows_dir = Path(".github/workflows")
    workflows_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize pipeline structure
    pipeline = {
        "name": "CI/CD Pipeline",
        "on": {"push": {}},
        "jobs": {}
    }

    # Add build steps
    for step in config["build_steps"]:
        template_path = f"templates/{config['technology']}/{step}.yml"
        with open(template_path) as t:
            pipeline["jobs"][step] = {
                "runs-on": "ubuntu-latest",
                "steps": [
                    {"uses": "actions/checkout@v4"},
                    {"name": f"Run {step}", "run": t.read().strip()}
                ]
            }

    # Add deployment
    with open(f"templates/deployment/{config['deploy_method']}.yml") as d:
        pipeline["jobs"]["deploy"] = {
            "needs": config["build_steps"],
            "runs-on": "ubuntu-latest",
            "steps": [
                {"uses": "actions/checkout@v4"},
                {"name": "Deploy", "run": d.read().strip()}
            ]
        }

    # Write properly formatted YAML
    with open(workflows_dir / "pipeline.yml", "w") as f:
        yaml.dump(pipeline, f, sort_keys=False, default_flow_style=False, width=float("inf"))

if __name__ == "__main__":
    generate_pipeline()
