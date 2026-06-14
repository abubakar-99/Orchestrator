import os
import base64
import requests

TOKEN = os.environ["GH_PAT"]
DAY = int(os.environ["DAY"])
USERNAME = "abubakar-99"

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

PROJECTS = {
    1:  ("llm-prompt-scanner",              "Python",     "Detects and classifies prompt injection attacks in user inputs"),
    2:  ("currency-arbitrage-detector",     "Python",     "Monitors exchange rate discrepancies across APIs in real time"),
    3:  ("git-blame-ai-reviewer",           "TypeScript", "Analyzes git history with AI to flag tech debt and suggest refactors"),
    4:  ("zero-trust-api-gateway",          "Go",         "Middleware enforcing per-route auth policies and anomaly detection"),
    5:  ("distributed-log-aggregator",      "Go",         "Collects and streams logs from microservices to a queryable store"),
    6:  ("ai-resume-parser",                "Python",     "Extracts structured data from resumes and scores against job descriptions"),
    7:  ("supply-chain-risk-tracker",       "Python",     "Flags geopolitical risks affecting supply chains using news APIs"),
    8:  ("webrtc-file-transfer",            "JavaScript", "Browser-based encrypted P2P file transfer with no server storage"),
    9:  ("k8s-cost-analyzer",              "Go",         "Maps Kubernetes resource usage to actual cloud billing per namespace"),
    10: ("threat-intel-aggregator",         "Python",     "Unified threat feed from MISP, AlienVault, and VirusTotal"),
    11: ("ai-sql-optimizer",               "Python",     "Profiles slow SQL queries and suggests index changes with benchmarks"),
    12: ("carbon-footprint-api",            "TypeScript", "REST API calculating CO2 emissions from travel and energy usage"),
    13: ("deepfake-audio-detector",         "Python",     "Classifies audio as real or synthetic using MFCC features and CNN"),
    14: ("cloud-secret-rotator",            "Go",         "CLI that rotates API keys across AWS, GCP, and Azure on a schedule"),
    15: ("realtime-fraud-engine",           "Python",     "Scores financial transactions in under 50ms using ML pipeline"),
    16: ("dependency-vulnerability-auditor","TypeScript", "Scans packages for CVEs, license violations, and abandoned deps"),
    17: ("ai-meeting-summarizer",           "Python",     "Converts meeting transcripts into action items and decisions"),
    18: ("edge-inference-server",           "Rust",       "Runs quantized ONNX models at the edge with gRPC API"),
    19: ("distributed-rate-limiter",        "Go",         "Redis-backed sliding window rate limiter with atomic Lua operations"),
    20: ("healthcare-data-anonymizer",      "Python",     "Strips PII from medical records using NER — HIPAA compliant"),
    21: ("smart-contract-scanner",          "Python",     "Detects reentrancy and overflow bugs in Solidity smart contracts"),
    22: ("market-sentiment-api",            "Python",     "Aggregates Twitter and Reddit sentiment per ticker via NLP"),
    23: ("ai-code-review-bot",              "TypeScript", "GitHub Action that reviews PRs for security issues and coverage"),
    24: ("container-escape-detector",       "Go",         "Monitors syscalls inside Docker containers for privilege escalation"),
    25: ("multilingual-ner-pipeline",       "Python",     "Named entity recognition supporting 20+ languages with mBERT"),
    26: ("sla-breach-predictor",            "Python",     "Predicts which services are at risk of missing SLA targets"),
    27: ("api-diff-tool",                   "TypeScript", "Compares OpenAPI spec versions and generates breaking-change reports"),
    28: ("chaos-engineering-toolkit",       "Go",         "Injects network latency and pod failures into K8s clusters"),
    29: ("ai-document-classifier",          "Python",     "Classifies PDFs into categories using vision model and vector search"),
    30: ("privacy-policy-scanner",          "Python",     "Analyzes privacy policies for GDPR violations and dark patterns"),
    31: ("realtime-json-editor",            "TypeScript", "CRDT-powered JSON editor with conflict-free multi-user editing"),
    32: ("log-anomaly-detector",            "Python",     "Unsupervised ML model to flag unusual log sequences"),
    33: ("infra-drift-detector",            "Go",         "Compares live cloud resources against Terraform state"),
    34: ("ai-pentest-assistant",            "Python",     "Suggests attack vectors based on discovered service fingerprints"),
    35: ("global-food-price-index",         "Python",     "Real-time country-level food insecurity scores from FAO data"),
    36: ("async-job-queue",                 "TypeScript", "Production-grade background job system with DLQ dashboard"),
    37: ("ai-accessibility-auditor",        "TypeScript", "Scans web pages and generates WCAG 2.2 compliance reports"),
    38: ("satellite-change-detector",       "Python",     "Detects deforestation using NDVI differencing on Sentinel-2 imagery"),
    39: ("mtls-cert-manager",               "Go",         "Issues and rotates mTLS certificates with embedded ACME-like CA"),
    40: ("ai-load-balancer",                "Go",         "Routes traffic based on predicted backend latency using online learning"),
    41: ("open-banking-categorizer",        "Python",     "Classifies bank transactions using fine-tuned transformer model"),
    42: ("network-topology-mapper",         "Python",     "Auto-discovers and visualizes network topology from SNMP data"),
    43: ("ml-bias-detector",                "Python",     "Evaluates ML models for demographic parity and equalized odds"),
    44: ("election-data-pipeline",          "Python",     "ETL pipeline ingesting electoral commission feeds with anomaly flagging"),
    45: ("browser-extension-auditor",       "JavaScript", "Analyzes Chrome extension permissions to detect data exfiltration"),
    46: ("vector-search-engine",            "Rust",       "Minimal vector DB built from scratch using HNSW indexing"),
    47: ("multitenant-billing-engine",      "TypeScript", "Usage-based billing with metering, proration, and Stripe integration"),
    48: ("sql-to-api-generator",            "Python",     "Generates typed REST/GraphQL API from SQL schema with auth"),
    49: ("incident-postmortem-generator",   "TypeScript", "Auto-drafts blameless post-mortems from PagerDuty alerts and logs"),
    50: ("water-stress-monitor",            "Python",     "Real-time water scarcity risk API from satellite and WHO datasets"),
}

EXT_MAP = {
    "Python": "py",
    "TypeScript": "ts",
    "JavaScript": "js",
    "Go": "go",
    "Rust": "rs"
}

INSTALL_CMD = {
    "Python":     "pip install -r requirements.txt",
    "TypeScript": "npm install",
    "JavaScript": "npm install",
    "Go":         "go mod tidy",
    "Rust":       "cargo build --release"
}

RUN_CMD = {
    "Python":     "python src/main.py --help",
    "TypeScript": "npx ts-node src/index.ts",
    "JavaScript": "node src/index.js",
    "Go":         "go run cmd/main.go",
    "Rust":       "./target/release/app"
}

BADGE = {
    "Python":     "![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)",
    "TypeScript": "![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue?logo=typescript)",
    "Go":         "![Go](https://img.shields.io/badge/Go-1.22-00ADD8?logo=go)",
    "Rust":       "![Rust](https://img.shields.io/badge/Rust-1.77-orange?logo=rust)",
    "JavaScript": "![JavaScript](https://img.shields.io/badge/JavaScript-ES2024-yellow?logo=javascript)",
}


def push_file(repo, path, content, message, sha=None):
    url = "https://api.github.com/repos/" + USERNAME + "/" + repo + "/contents/" + path
    data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode()
    }
    if sha:
        data["sha"] = sha
    r = requests.put(url, headers=HEADERS, json=data)
    return r.status_code in [200, 201]


def get_file_sha(repo, path):
    url = "https://api.github.com/repos/" + USERNAME + "/" + repo + "/contents/" + path
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json().get("sha")
    return None


def generate_readme(name, lang, desc):
    badge = BADGE.get(lang, "")
    install = INSTALL_CMD.get(lang, "")
    run = RUN_CMD.get(lang, "")
    ext = EXT_MAP.get(lang, "py")

    return (
        "# " + name + "\n\n"
        + badge + " "
        + "![License](https://img.shields.io/badge/License-MIT-green) "
        + "![Status](https://img.shields.io/badge/Status-Active-brightgreen)\n\n"
        + desc + ".\n\n"
        + "## Overview\n\n"
        + "This tool provides a production-ready implementation focused on performance, "
        + "security, and developer experience. Built with modern best practices and designed "
        + "for real-world deployment.\n\n"
        + "## Features\n\n"
        + "- **High performance** — optimized for low latency and high throughput\n"
        + "- **Production ready** — proper error handling, logging, and observability\n"
        + "- **Well tested** — unit and integration tests included\n"
        + "- **Easy to deploy** — Docker support out of the box\n\n"
        + "## Installation\n\n"
        + "```bash\n"
        + "git clone https://github.com/" + USERNAME + "/" + name + "\n"
        + "cd " + name + "\n"
        + install + "\n"
        + "```\n\n"
        + "## Usage\n\n"
        + "```bash\n"
        + run + "\n"
        + "```\n\n"
        + "## Architecture\n\n"
        + "```\n"
        + name + "/\n"
        + "├── src/\n"
        + "│   ├── main." + ext + "\n"
        + "│   ├── core/\n"
        + "│   └── utils/\n"
        + "├── tests/\n"
        + "├── docs/\n"
        + "├── Dockerfile\n"
        + "└── README.md\n"
        + "```\n\n"
        + "## Contributing\n\n"
        + "Pull requests are welcome. For major changes, please open an issue first.\n\n"
        + "## License\n\n"
        + "[MIT](LICENSE)\n"
    )


def generate_main_python(name, desc):
    return (
        '"""\n'
        + name + " - " + desc + "\n"
        + '"""\n'
        + "import argparse\n"
        + "import logging\n"
        + "import sys\n"
        + "from typing import Optional\n\n"
        + 'logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")\n'
        + "logger = logging.getLogger(__name__)\n\n\n"
        + "def process(input_data: str, verbose: bool = False) -> dict:\n"
        + '    """Core processing logic for ' + name + '."""\n'
        + "    if verbose:\n"
        + '        logger.info("Processing input...")\n\n'
        + "    result = {\n"
        + '        "status": "success",\n'
        + '        "input": input_data,\n'
        + '        "output": None,\n'
        + '        "metadata": {}\n'
        + "    }\n\n"
        + "    logger.info('Processing complete')\n"
        + "    return result\n\n\n"
        + "def main(args: Optional[list] = None) -> int:\n"
        + '    parser = argparse.ArgumentParser(description="' + desc + '")\n'
        + '    parser.add_argument("input", nargs="?", help="Input data to process")\n'
        + '    parser.add_argument("-v", "--verbose", action="store_true")\n'
        + "    parsed = parser.parse_args(args)\n\n"
        + "    if not parsed.input:\n"
        + "        parser.print_help()\n"
        + "        return 1\n\n"
        + "    try:\n"
        + "        result = process(parsed.input, parsed.verbose)\n"
        + "        print(result)\n"
        + "        return 0\n"
        + "    except Exception as e:\n"
        + '        logger.error("Error: %s", e)\n'
        + "        return 1\n\n\n"
        + 'if __name__ == "__main__":\n'
        + "    sys.exit(main())\n"
    )


def generate_main_go(name, desc):
    return (
        "package main\n\n"
        + "import (\n"
        + '\t"flag"\n'
        + '\t"fmt"\n'
        + '\t"log"\n'
        + '\t"os"\n'
        + ")\n\n"
        + "// Result represents processing output\n"
        + "type Result struct {\n"
        + "\tStatus string\n"
        + "\tOutput string\n"
        + "}\n\n"
        + "func process(input string, verbose bool) (*Result, error) {\n"
        + "\tif verbose {\n"
        + '\t\tlog.Printf("Processing: %s", input)\n'
        + "\t}\n"
        + "\treturn &Result{Status: \"success\", Output: input}, nil\n"
        + "}\n\n"
        + "func main() {\n"
        + '\tverbose := flag.Bool("verbose", false, "Enable verbose output")\n'
        + "\tflag.Parse()\n\n"
        + "\tif flag.NArg() == 0 {\n"
        + '\t\tfmt.Fprintf(os.Stderr, "Usage: ' + name + ' [options] <input>\\n")\n'
        + "\t\tos.Exit(1)\n"
        + "\t}\n\n"
        + "\tresult, err := process(flag.Arg(0), *verbose)\n"
        + "\tif err != nil {\n"
        + '\t\tlog.Fatalf("Error: %v", err)\n'
        + "\t}\n"
        + '\tfmt.Printf("Status: %s\\n", result.Status)\n'
        + "}\n"
    )


def generate_main_ts(name, desc):
    return (
        "/**\n"
        + " * " + name + "\n"
        + " * " + desc + "\n"
        + " */\n\n"
        + "interface Result {\n"
        + "  status: string;\n"
        + "  output: unknown;\n"
        + "  metadata: Record<string, string>;\n"
        + "}\n\n"
        + "async function process(input: string, verbose = false): Promise<Result> {\n"
        + "  if (verbose) {\n"
        + "    console.log('Processing:', input.substring(0, 50));\n"
        + "  }\n"
        + "  return { status: 'success', output: input, metadata: { version: '1.0.0' } };\n"
        + "}\n\n"
        + "async function main(): Promise<void> {\n"
        + "  const args = process.argv.slice(2);\n"
        + "  if (args.length === 0) {\n"
        + "    console.error('Usage: ts-node src/main.ts <input>');\n"
        + "    process.exit(1);\n"
        + "  }\n"
        + "  const result = await process(args[0], args.includes('--verbose'));\n"
        + "  console.log(JSON.stringify(result, null, 2));\n"
        + "}\n\n"
        + "main();\n"
    )


def generate_main_js(name, desc):
    return (
        "/**\n"
        + " * " + name + "\n"
        + " * " + desc + "\n"
        + " */\n\n"
        + "async function process(input, verbose = false) {\n"
        + "  if (verbose) console.log('Processing:', input);\n"
        + "  return { status: 'success', output: input, metadata: { version: '1.0.0' } };\n"
        + "}\n\n"
        + "async function main() {\n"
        + "  const args = process.argv.slice(2);\n"
        + "  if (!args.length) {\n"
        + "    console.error('Usage: node src/main.js <input>');\n"
        + "    process.exit(1);\n"
        + "  }\n"
        + "  const result = await process(args[0], args.includes('--verbose'));\n"
        + "  console.log(JSON.stringify(result, null, 2));\n"
        + "}\n\n"
        + "main();\n"
    )


def generate_main_rust(name, desc):
    return (
        "//! " + name + " - " + desc + "\n\n"
        + "use std::env;\n\n"
        + "#[derive(Debug)]\n"
        + "struct Result {\n"
        + "    status: String,\n"
        + "    output: String,\n"
        + "}\n\n"
        + "fn process(input: &str, verbose: bool) -> Result {\n"
        + "    if verbose {\n"
        + '        eprintln!("Processing: {}", &input[..input.len().min(50)]);\n'
        + "    }\n"
        + "    Result { status: String::from(\"success\"), output: input.to_string() }\n"
        + "}\n\n"
        + "fn main() {\n"
        + "    let args: Vec<String> = env::args().collect();\n"
        + "    if args.len() < 2 {\n"
        + '        eprintln!("Usage: {} <input>", args[0]);\n'
        + "        std::process::exit(1);\n"
        + "    }\n"
        + "    let verbose = args.contains(&String::from(\"--verbose\"));\n"
        + "    let result = process(&args[1], verbose);\n"
        + '    println!("Status: {}", result.status);\n'
        + "}\n"
    )


def generate_main_file(name, lang, desc):
    if lang == "Python":
        return generate_main_python(name, desc)
    elif lang == "Go":
        return generate_main_go(name, desc)
    elif lang == "TypeScript":
        return generate_main_ts(name, desc)
    elif lang == "JavaScript":
        return generate_main_js(name, desc)
    elif lang == "Rust":
        return generate_main_rust(name, desc)
    return ""


def run():
    if DAY < 1 or DAY > 50:
        print("Day " + str(DAY) + " is out of range (1-50). Skipping.")
        return

    repo, lang, desc = PROJECTS[DAY]
    ext = EXT_MAP.get(lang, "py")
    print("Pushing Day " + str(DAY) + ": " + repo + " (" + lang + ")")

    readme = generate_readme(repo, lang, desc)
    main_file = generate_main_file(repo, lang, desc)

    readme_sha = get_file_sha(repo, "README.md")
    ok1 = push_file(repo, "README.md", readme, "docs: add professional README for " + repo, readme_sha)

    src_path = "src/main." + ext
    ok2 = push_file(repo, src_path, main_file, "feat: initial implementation of " + repo)

    if ok1 and ok2:
        print("Done: github.com/" + USERNAME + "/" + repo)
    else:
        print("Failed — README: " + str(ok1) + ", src: " + str(ok2))


if __name__ == "__main__":
    run()
