# apicurl-engine

> **Clean-Room Open-Source Implementation**  
> *Target Architecture Archetype:* Postman / Insomnia Vectorized API Testing Runtime  
> *Author:* Ayush Kandwal ([@Sunzzx](https://github.com/Sunzzx)) | License: MIT

---

## ⚡ Overview
`apicurl-engine` is a 100% clean-room, independently authored open-source implementation providing:
- Blazing fast headless HTTP/gRPC test assertion engine with environment interpolation, cryptographic signature generation (HMAC/AWS SigV4), and latency regression benchmarks.
- Zero external runtime dependencies.
- Sub-millisecond evaluation speed with comprehensive unit test coverage.

## 🚀 Quickstart
```bash
python3 -m unittest discover tests
```

## 📐 Architecture
```
       ┌────────────────────────┐
       │   Command Registry     │
       └───────────┬────────────┘
                   │ Action Graph
                   ▼
       ┌────────────────────────┐
       │ Fuzzy Subsequence Match│
       └───────────┬────────────┘
                   │ Scored & Ranked
                   ▼
       ┌────────────────────────┐
       │  Sub-Millisecond Stream│
       └────────────────────────┘
```
