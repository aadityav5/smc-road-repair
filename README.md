# SMC Road Repair - Smart Road Reporting System

A web-based road damage reporting application that uses AI to analyze photos of road damage. The frontend integrates with a Lightning.ai deployed model for intelligent damage classification.

## 🚀 Quick Start - Frontend Access

### Option 1: GitHub Pages (Recommended)
The frontend is automatically deployed via GitHub Pages:
```
https://aadityav5.github.io/smc-road-repair/
```

### Option 2: Local Development
Run locally using Python's built-in server:
```bash
cd smc-road-repair
python3 -m http.server 8080
# Open http://localhost:8080 in your browser
```

Or using Node.js:
```bash
npx serve .
# Open http://localhost:3000 in your browser
```

## 🤖 Lightning.ai Integration

The frontend connects to the Lightning.ai deployed model at:
```
https://11434-dep-01kgm1ghq8p0d4c2533jdf4jcg-d.cloudspaces.litng.ai
```

### How to Verify Lightning.ai is Receiving Requests

1. **Open Browser Developer Tools**
   - Chrome/Edge: Press `F12` or `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Option+I` (Mac)
   - Go to the **Console** tab

2. **Upload a Photo**
   - Click "📷 Tap to Take Photo" and select an image
   - Watch the console for detailed logs

3. **Look for These Log Messages**:
   ```
   🚀 [Lightning.ai] Starting image analysis...
   🔗 [Lightning.ai] API URL: https://11434-dep-01kgm1ghq8p0d4c2533jdf4jcg-d.cloudspaces.litng.ai
   📦 [Lightning.ai] Image data size: XXX KB
   📡 [Lightning.ai] Attempting request to: https://...
   ⏱️ [Lightning.ai] Response received in XXXms
   📊 [Lightning.ai] Response status: 200 OK
   ✅ [Lightning.ai] Successful response: {...}
   ```

4. **Check Network Tab**
   - Go to the **Network** tab in Developer Tools
   - Filter by "Fetch/XHR"
   - You'll see POST requests to the Lightning.ai endpoint
   - Click on a request to see details (Headers, Payload, Response)

### API Request Format

The frontend sends requests in this format:
```json
{
  "image": "<base64-encoded-image-data>"
}
```

### Expected API Response Format

The model should return one of these formats:
```json
// Format 1 - Direct
{
  "severity": "High",
  "issue": "Pothole",
  "confidence": 0.95
}

// Format 2 - Nested
{
  "prediction": {
    "severity": "Medium",
    "issue": "Crack",
    "confidence": 0.87
  }
}

// Format 3 - Classification
{
  "class": "Pothole",
  "score": 0.92
}
```

## 🔧 Configuration

To use a different Lightning.ai endpoint, update the URL in `index.html`:
```javascript
const LIGHTNING_AI_API_URL = "https://your-lightning-ai-url.cloudspaces.litng.ai";
```

## 📱 Features

- **Photo Capture**: Take or upload photos of road damage
- **AI Analysis**: Automatic damage classification (Pothole, Crack, Surface Wear)
- **Severity Assessment**: High/Medium/Low severity detection
- **GPS Location**: Automatic location detection
- **Fallback Mode**: Local analysis if API is unavailable

## 🛠️ Troubleshooting

### "Fallback analysis - API unavailable" message

This means the Lightning.ai API is not reachable. Check:
1. Is the Lightning.ai model running?
2. Is the URL correct in the configuration?
3. Are there CORS headers enabled on the Lightning.ai server?

### CORS Issues

If you see CORS errors in the console, ensure your Lightning.ai model includes these headers:
```python
# In your Lightning.ai server
response.headers["Access-Control-Allow-Origin"] = "*"
response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
response.headers["Access-Control-Allow-Headers"] = "Content-Type"
```