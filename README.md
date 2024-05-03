# Financial_Agents

This project aims to create an agentic workflow to help users improve their finances. Part of Google AI Hackathon.

## Topics

1. [Overview](#overview)
2. [Goals](#goals)
3. [Scope and Context](#scope-and-context)
4. [System Design](#system-design)
5. [Alternatives Considered](#alternatives-considered)
6. [Cross-cutting Concerns](#cross-cutting-concerns)
7. [Learning Logs](#learning-logs)
8. [Resources](#resources)

---

## Overview

The Financial_Agents project empowers users to improve their financial well-being through an innovative workflow.
Developed for the Google AI Hackathon, it uses advanced technology like Gemini LLM to streamline financial management and offer personalized assistance.

## Goals

The main goal of the Financial_Agents project is to create a user-friendly workflow for informed financial decisions. Using Gemini LLM, it aims to:

1. Allow users to ask finance-related questions in natural language.

2. Fetch relevant data from a specific financial database.

3. Automatically extract important information from bank email notifications.

4. Populate the financial database with key transaction details.

5. Promote financial literacy and responsibility by facilitating smooth interaction between users and the financial system.

## Scope and Context

The Financial_Agents project operates at the intersection of financial management and artificial intelligence. It aims to streamline and personalize financial assistance in a complex data-driven landscape. Key aspects include:

- **Financial Management Landscape:** Encompassing budgeting, expense tracking, investment management, and financial planning.

- **AI Integration:** Utilizing Gemini LLM for intelligent automation and natural language understanding.

- **Email Notification Parsing:** Involves extracting transaction details from banking email notifications for database population.

- **User-Centric Approach:** Prioritizing personalized assistance through conversational interfaces and data-driven insights.

- **Scope:** Developing an agentic workflow enabling users to ask financial queries, receive insights, and automate data extraction, but excluding specific banking systems integration or regulatory compliance.

## System Design

![image](https://private-user-images.githubusercontent.com/74464814/327626367-9e06a3f7-27d7-4311-92b4-2d391d5149c4.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTQ2OTk5NjQsIm5iZiI6MTcxNDY5OTY2NCwicGF0aCI6Ii83NDQ2NDgxNC8zMjc2MjYzNjctOWUwNmEzZjctMjdkNy00MzExLTkyYjQtMmQzOTFkNTE0OWM0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTAzVDAxMjc0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJlZDcxZGM4YTM4N2NmMDg4YjhlMTVhYmIwY2NmYTNhMGY4ZWMyYTE3NzBkYjNmZDUyMGZmNTEwZWMyYmI4YTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.qKdi1-Dt2e7Hp_Qhv7yfS5_RqqXbfNIV2NaZFWWYwV0)

## Alternatives Considered

Several alternatives were considered for the Financial_Agents project, each with unique trade-offs:

- **Manual Data Entry:** Allows users to input transaction details manually, offering flexibility but risking errors and requiring significant effort.

- **Third-Party API Integration:** Offers real-time data access but introduces dependencies and potential security concerns.

- **Rule-Based Parsing:** Simplifies implementation but lacks adaptability and may require frequent maintenance.

- **Machine Learning Email Parsing:** Utilizes natural language processing for automated extraction, offering accuracy and scalability. Chosen for its alignment with project goals of automation and user-centric design.

## Cross-cutting Concerns

The Financial_Agents project addresses cross-cutting concerns including security, privacy, and observability:

- **Security:** Various measures like encryption and access control safeguard sensitive financial information against unauthorized access and data breaches.

- **Privacy:** Data minimization and anonymization protect user privacy, while explicit consent ensures compliance with privacy regulations.

- **Observability:** Logging, monitoring, and alerting mechanisms provide insights into system performance and enable proactive issue resolution.

## Learning Logs

| Date | Learning |
|------|----------|
|      |          |

## Resources

- [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)

---

## Version Management

To create a changelog, run:

```bash
cz changelog
```

And to bump the changelog version after performing modifications, run:

```bash
cz bump
```
