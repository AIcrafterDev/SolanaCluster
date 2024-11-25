<p align="center">
  <img src="https://i.postimg.cc/s2qJvxcN/logg2.png" alt="Cluster Logo" width="200"/>
</p>

<h1 align="center">Cluster: Solana AI Trading Agent Framework</h1>

<p align="center">
  <b>AI-driven Solana trading made simple.</b><br>
  Natural language commands to automate transfers, DEX trading, sniping, and portfolio management.
</p>

---

## **Key Features**

### **🤖 AI-Powered Command Understanding**
Cluster interprets natural language commands to execute blockchain operations, including:

#### **Examples:**
- **Transfer Funds**:  
  *Command*: `Send $250 worth of Solana to H2aPpY...`  
  *Response*: `Sending 10.000000 SOL (equivalent to $250.00)...`

- **Check Market Prices**:  
  *Command*: `What's the price of SOL?`  
  *Response*: `Current SOL price: $250.00 USDC`

- **Trade on DEX**:  
  *Command*: `Buy half my USDC balance in SOL on Raydium`  
  *Response*: `Executing trade on Raydium DEX to buy 2 Solana...`

- **Snipe Tokens**:  
  *Command*: `Snipe HYPE token on pump.fun`  
  *Response*: `Monitoring HYPE token... Buy opportunity detected! Executing purchase...`

- **Portfolio Management**:  
  *Command*: `Show my portfolio balance`  
  *Response*:  
  ```
  Current Portfolio:
  - SOL: 25.5
  - USDC: 1000
  - HYPE: 50000
  ```

---

## **Setup Instructions**

### **Prerequisites**

1. **Operating System**: Linux/MacOS/Windows Subsystem for Linux (WSL recommended).
2. **Python Version**: Python 3.9 or higher.
3. **Tools Required**:
   - Git
   - Virtualenv
   - Node.js (optional for UI integrations).

---

### **Installation**

#### **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/cluster.git
cd cluster
```

#### **Step 2: Install Dependencies**

1. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Use venv\\Scripts\\activate on Windows
   ```

2. **Install Required Libraries**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements/base.txt
   ```

3. **Install Development Tools (Optional)**:
   ```bash
   pip install -r requirements/dev.txt
   ```

---

### **Step 3: Configure Environment Variables**

1. **Copy `.env.example`**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env`**:
   ```bash
   nano .env
   ```

   **Example Configuration**:
   ```
   # RPC URL for Solana Network
   RPC_URL=https://api.mainnet-beta.solana.com

   # Path to Wallet Keypair
   WALLET_KEYPAIR=/path/to/keypair.json

   # Custom API Keys (optional for market analysis)
   COINGECKO_API_KEY=your_coingecko_api_key
   PUMP_FUN_API_KEY=your_pump_fun_api_key
   ```

---

### **Step 4: Initialize Environment**
Run the initialization script:
```bash
./scripts/init_env.sh
```

This ensures `.env` is properly configured and linked.

---

### **Step 5: Launch the Agent**
Start Cluster in interactive mode:
```bash
./scripts/start_cluster.sh
```

---

## **Usage**

### **1. Interactive Command Mode**
Type natural language commands directly to interact with the framework.

#### **Examples**:
```text
> Send $250 worth of Solana to H2aPpY...
Sending 10.000000 SOL (equivalent to $250.00)...
Transaction submitted! Hash: abc123...

> What's the price of SOL?
Current SOL price: $250.00 USDC

> Buy half my USDC balance in SOL on Raydium
Executing trade on Raydium DEX to buy 2 Solana...
Transaction submitted! Hash: xyz789...

> Snipe HYPE token on pump.fun
Monitoring HYPE token... Buy opportunity detected! Executing purchase...
Transaction submitted! Hash: def456...

> Show my portfolio balance
Current Portfolio:
- SOL: 25.5
- USDC: 1000
- HYPE: 50000
```

---

### **2. Command-Line Actions**

#### **Transfer Funds**
```bash
python -m cluster transfer <amount> <recipient>
```

- **Example**:
  ```bash
  python -m cluster transfer 1.5 H2aPpYreCeIvErPkbXCwHDGrGfMHTRmPjW3
  ```

#### **Trade on DEX**
```bash
python -m cluster dex swap <amount> <token_in> <token_out>
```

- **Example**:
  ```bash
  python -m cluster dex swap 50 USDC SOL
  ```

#### **Token Sniping**
```bash
python -m cluster snipe <keyword>
```

- **Example**:
  ```bash
  python -m cluster snipe HYPE
  ```

#### **Portfolio Management**
```bash
python -m cluster portfolio show
```

- **Example**:
  ```bash
  python -m cluster portfolio show
  ```

---

## **Advanced Configuration**

### **Custom AI Models**
Integrate your own AI models for intent recognition or trading predictions by modifying the following:
- **`nlp.py`**: Update the NLP pipeline for custom logic.
- **`intent_classifier.py`**: Replace or fine-tune intent classification models.

---

## **Testing**

### **Run All Tests**
```bash
pytest
```

### **Lint the Code**
```bash
flake8
```

---

## **Roadmap**

1. **New Features**:
   - Advanced trading strategies (e.g., stop-loss, take-profit).
   - Cross-chain support for Ethereum and Binance Smart Chain.

2. **AI Enhancements**:
   - Add GPT-based market trend predictions.

3. **Web-Based GUI**:
   - Develop a user-friendly web dashboard for non-CLI users.

---

## **Contributing**

We welcome contributions! Please:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## **License**

Cluster is licensed under the [MIT License](LICENSE).

---

<p align="center">
  <b>Start trading smarter with <i>Cluster</i>! 🚀</b>
</p>
