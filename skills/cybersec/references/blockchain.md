# Smart Contract and DeFi Security

> Source: huggingface.co/datasets/Vyber07/cyber-security (Apache-2.0). Community-curated reference; verify commands and versions before use.

## How to perform security audit of Ethereum smart contracts?

#### Smart Contract Security Audit

##### Static Analysis
```bash
# Slither
slither .
slither-check-erc .

# Mythril
myth analyze contract.sol

# Securify
securify contract.sol

# Oyente
oyente contract.sol
```

##### Common Vulnerabilities

###### 1. Reentrancy
```solidity
// Vulnerable
function withdraw() public {
    uint amount = balances[msg.sender];
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
    balances[msg.sender] = 0;  // State change after external call
}

// Fixed
function withdraw() public {
    uint amount = balances[msg.sender];
    balances[msg.sender] = 0;  // State change before external call
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
}
```

###### 2. Integer Overflow/Underflow
```solidity
// Vulnerable
function transfer(address to, uint256 amount) public {
    balances[msg.sender] -= amount;
    balances[to] += amount;
}

// Fixed (use SafeMath or Solidity 0.8+)
function transfer(address to, uint256 amount) public {
    require(balances[msg.sender] >= amount);
    balances[msg.sender] -= amount;
    balances[to] += amount;
}
```

###### 3. Access Control
```solidity
// Check for:
- Missing onlyOwner modifiers
- Unprotected functions
- Centralization risks
```

###### 4. Front-Running
```solidity
// Check for:
- Transaction ordering dependence
- Time-of-check to time-of-use
- Commit-reveal schemes
```

##### Testing
```bash
# Unit tests
truffle test

# Fuzzing
echidna contract.sol

# Formal verification
certora contract.sol
```

##### Tools
- Slither
- Mythril
- Securify
- Echidna
- Certora
- Manticore
- Oyente
