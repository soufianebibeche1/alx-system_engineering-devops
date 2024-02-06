# Project: Exploring Infrastructure - What Happens When You Type google.com in Your Browser and Press Enter

## Introduction
This project aims to explore the infrastructure side, specifically focusing on what happens when a user types "google.com" in their browser and presses Enter. As a Full-Stack Software Engineer, understanding the underlying workings of the software system, including network, servers, and security aspects, is crucial.

## Overview
When a user types "google.com" in their browser and presses Enter, several steps occur behind the scenes, involving network protocols, DNS resolution, server communication, and web page rendering. Let's break down the process:

### Domain Name System (DNS) Resolution
1. The browser sends a DNS resolution request to the local DNS resolver or DNS server to translate the domain name "google.com" into an IP address.
2. The local DNS resolver checks its cache for a matching IP address. If not found, it recursively queries authoritative DNS servers until it obtains the IP address associated with "google.com."
3. Once the IP address is resolved, it is returned to the browser.

### Establishing a Connection
4. The browser initiates a TCP connection to the IP address obtained from DNS resolution, typically on port 80 for HTTP or port 443 for HTTPS.
5. The TCP handshake occurs between the client (browser) and the server (Google's web server), establishing a reliable communication channel.

### Sending HTTP Request
6. The browser constructs an HTTP request, including the desired resource (e.g., "/" for the homepage) and additional headers.
7. The HTTP request is sent over the established TCP connection to the Google server.

### Processing the Request
8. Google's web server receives the HTTP request and processes it. It may involve routing the request to the appropriate backend servers, handling load balancing, and executing any server-side logic.

### Generating Response
9. After processing the request, the server generates an HTTP response, typically containing HTML, CSS, JavaScript, and other resources required to render the webpage.
10. The HTTP response is sent back to the browser over the established TCP connection.

### Rendering the Webpage
11. The browser receives the HTTP response and begins parsing the HTML content.
12. As the browser parses the HTML, it fetches additional resources (e.g., CSS, JavaScript, images) referenced in the document.
13. The browser renders the webpage based on the received content and executes any JavaScript code present.

## Conclusion
Understanding the sequence of events that occur when a user enters a URL in their browser provides insights into the underlying infrastructure and protocols involved in serving web content. This knowledge is essential for Full-Stack Software Engineers to build robust and efficient web applications.

---
**Author:** Soufiane Bibeche

**Date:** Feb 06, 2024 4:00 AM

**Project Deadline:** Feb 12, 2024 4:00 AM
