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

The Financial_Agents project is a pioneering endeavor that aims to empower users in enhancing their financial well-being through an innovative agentic workflow.
Developed as part of the Google AI Hackathon, this project leverages advanced technologies, including Gemini LLM, to streamline financial management processes and provide personalized assistance to users.

## Goals

The primary objective of the Financial_Agents project is to create an intuitive and efficient workflow that enables users to make informed financial decisions.
By harnessing the capabilities of Gemini LLM, the project seeks to:

1. Enable users to pose queries regarding their finances in natural language.

2. Retrieve relevant data from a designated financial database.

3. Automate the extraction of pertinent information from email notifications issued by banking institutions.

4. Populate the financial database with essential transaction details, including price, date, entity, and service.

5. Facilitate seamless interaction between users and the financial system to foster financial literacy and responsibility.

## Scope and Context

The Financial_Agents project operates within the domain of financial management and artificial intelligence.
It addresses the growing need for streamlined and personalized financial assistance in an increasingly complex and data-driven landscape. Key aspects of the project's context and scope include:

- Financial Management Landscape: The project operates within the broader context of financial management, encompassing areas such as budgeting, expense tracking, investment management, and financial planning.

- Artificial Intelligence Integration: Leveraging advanced AI technologies, specifically Gemini LLM, the project aims to introduce intelligent automation and natural language understanding capabilities to enhance user interactions and decision-making processes.

- Email Notification Parsing: A significant component of the project involves parsing email notifications from banking institutions to extract essential transaction details. This process involves monitoring email servers, extracting relevant information, and populating a centralized financial database.

- User-Centric Approach: The project prioritizes user experience and aims to provide personalized financial assistance tailored to individual needs and preferences. Through conversational interfaces and data-driven insights, users can interact with the system in a seamless and intuitive manner.

- Scope: The scope of the project encompasses the development and implementation of a comprehensive agentic workflow that enables users to pose financial queries, receive relevant insights, and automate transaction data extraction and organization. It does not extend to specific banking systems integration or regulatory compliance aspects, which may vary depending on regional or institutional requirements.

By focusing on these key aspects, the Financial_Agents project aims to address critical challenges in financial management while providing users with the tools and insights needed to achieve their financial goals effectively.

## System Design

![image](https://private-user-images.githubusercontent.com/74464814/327626367-9e06a3f7-27d7-4311-92b4-2d391d5149c4.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTQ2OTk5NjQsIm5iZiI6MTcxNDY5OTY2NCwicGF0aCI6Ii83NDQ2NDgxNC8zMjc2MjYzNjctOWUwNmEzZjctMjdkNy00MzExLTkyYjQtMmQzOTFkNTE0OWM0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTAzVDAxMjc0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJlZDcxZGM4YTM4N2NmMDg4YjhlMTVhYmIwY2NmYTNhMGY4ZWMyYTE3NzBkYjNmZDUyMGZmNTEwZWMyYmI4YTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.qKdi1-Dt2e7Hp_Qhv7yfS5_RqqXbfNIV2NaZFWWYwV0)

## Alternatives Considered

Several alternative approaches were considered during the design phase of the Financial_Agents project. Each alternative presented unique trade-offs and considerations, ultimately leading to the selection of the primary design outlined in this document.

- Manual Data Entry: One alternative considered was a manual data entry approach, where users would input transaction details manually into the system. While this approach offers flexibility and control over data entry, it introduces the risk of errors and requires significant user effort. Additionally, it lacks the automation and efficiency goals of the project.

- Third-Party API Integration: Another alternative explored was integrating with third-party financial APIs to retrieve transaction data directly from banking institutions. While this approach could provide real-time data access and reduce reliance on email notifications, it introduces dependencies on external services and potential security concerns. Moreover, it may limit the project's scalability and flexibility in supporting various banking systems.

- Rule-Based Parsing: A rule-based parsing approach for email notifications was also considered. This involves defining specific rules and patterns to extract transaction details from emails. While initially simpler to implement, this approach may lack the adaptability and accuracy required to handle diverse email formats and languages effectively. It could also require frequent maintenance to accommodate changes in email formats.

- Machine Learning Email Parsing: Lastly, a machine learning-based approach to email parsing, similar to the one employed in the project, was evaluated. This approach utilizes natural language processing and machine learning algorithms to extract transaction details from email notifications automatically. While more complex to implement initially, this approach offers greater flexibility, accuracy, and scalability, especially in handling diverse email formats and languages. Additionally, it aligns with the project's objectives of leveraging advanced AI technologies to enhance automation and user experience.

After careful evaluation of these alternatives, the decision was made to proceed with the machine learning-based email parsing approach due to its superior accuracy, scalability, and alignment with the project goals of automation and user-centric design. This approach enables the Financial_Agents project to deliver efficient and personalized financial assistance to users while minimizing manual effort and errors.

## Cross-cutting Concerns

### Security

- Security measures are implemented at various levels within the project to safeguard sensitive financial information and protect against unauthorized access or data breaches. These measures include:

- Encryption: All communication channels, including email notifications and database connections, are encrypted to prevent interception and unauthorized access to sensitive data.

- Access Control: Role-based access control mechanisms are employed to restrict access to the financial database and other critical system components, ensuring that only authorized personnel can interact with sensitive information.
Data Sanitization: Incoming data, particularly from email notifications, undergoes rigorous sanitization and validation processes to mitigate the risk of injection attacks and data manipulation.

### Privacy

Privacy considerations are central to the design of the Financial_Agents project, ensuring that user data is handled in compliance with applicable privacy regulations and best practices. Key privacy measures include:

- Data Minimization: Only essential transaction details are collected and stored in the financial database, minimizing the collection of personally identifiable information (PII) and reducing the risk of privacy breaches.
Anonymization: Where possible, user data is anonymized to protect user privacy while still enabling meaningful analysis and insights generation.

- User Consent: Users are informed about the types of data collected and their purposes, and explicit consent is obtained before accessing or processing any sensitive information.

### Observability

Observability mechanisms are incorporated into the Financial_Agents project to provide insights into system performance, reliability, and potential issues. These mechanisms include:

- Logging: Comprehensive logging is implemented throughout the system to record key events, errors, and user interactions, facilitating troubleshooting and auditing.

- Monitoring: Real-time monitoring tools are employed to track system metrics, such as transaction processing times, email parsing accuracy, and database performance, enabling proactive identification and resolution of issues.

- Alerting: Automated alerting systems notify administrators of any anomalies or critical events, enabling timely intervention and ensuring uninterrupted service availability.

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
