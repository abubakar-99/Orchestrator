#!/bin/bash
# Run this once to create all 50 public repos
# Usage: bash setup.sh YOUR_GITHUB_TOKEN

TOKEN=$1
USERNAME="abubakar-99"

REPOS=(
"llm-prompt-scanner"
"currency-arbitrage-detector"
"git-blame-ai-reviewer"
"zero-trust-api-gateway"
"distributed-log-aggregator"
"ai-resume-parser"
"supply-chain-risk-tracker"
"webrtc-file-transfer"
"k8s-cost-analyzer"
"threat-intel-aggregator"
"ai-sql-optimizer"
"carbon-footprint-api"
"deepfake-audio-detector"
"cloud-secret-rotator"
"realtime-fraud-engine"
"dependency-vulnerability-auditor"
"ai-meeting-summarizer"
"edge-inference-server"
"distributed-rate-limiter"
"healthcare-data-anonymizer"
"smart-contract-scanner"
"market-sentiment-api"
"ai-code-review-bot"
"container-escape-detector"
"multilingual-ner-pipeline"
"sla-breach-predictor"
"api-diff-tool"
"chaos-engineering-toolkit"
"ai-document-classifier"
"privacy-policy-scanner"
"realtime-json-editor"
"log-anomaly-detector"
"infra-drift-detector"
"ai-pentest-assistant"
"global-food-price-index"
"async-job-queue"
"ai-accessibility-auditor"
"satellite-change-detector"
"mtls-cert-manager"
"ai-load-balancer"
"open-banking-categorizer"
"network-topology-mapper"
"ml-bias-detector"
"election-data-pipeline"
"browser-extension-auditor"
"vector-search-engine"
"multitenant-billing-engine"
"sql-to-api-generator"
"incident-postmortem-generator"
"water-stress-monitor"
)

echo "Creating 50 public repos for $USERNAME..."

for REPO in "${REPOS[@]}"; do
  RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" \
    -X POST \
    -H "Authorization: token $TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/user/repos \
    -d "{\"name\":\"$REPO\",\"private\":false,\"auto_init\":true,\"license_template\":\"mit\"}")

  if [ "$RESPONSE" == "201" ]; then
    echo "✅ Created: $REPO"
  else
    echo "❌ Failed ($RESPONSE): $REPO"
  fi

  sleep 1
done

echo ""
echo "Done! Check github.com/$USERNAME"
