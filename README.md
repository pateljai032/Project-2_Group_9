# Project-2_Group_9

# Media Recommender System

## Overview
This repository contains a sophisticated Media Recommender System developed as part of a computer science project. It includes classes for managing media entities such as books and shows, and functionalities for loading data, generating recommendations, and displaying statistics.

## System Components
The system consists of several Python files each handling a specific part of the recommendation process:
- Media.py: Base class for all media types with common attributes like ID, title, and rating.
- Book.py: Subclass of Media, tailored for book handling, includes attributes like ISBN, author, and publisher.
- Show.py: Subclass of Media, designed for managing TV shows and movies, includes attributes like type, director, and actors.
- Recommender.py: Core engine that processes media data, manages recommendations, and stores them in dictionaries.
- RecommenderGUI.py: GUI layer for interacting with the recommender system, implemented using tkinter.
- `associated*.csv`: Datasets linking media content with associated metadata in varying sizes (10, 100, 1000).
- `books*.csv`: Datasets containing book information in varying sizes (10, 100, 1000).
- `shows*.csv`: Datasets containing TV show information in varying sizes (10, 100, 1000).

## Features
- Data Loading: Dynamic loading of books, shows, and associations data through a GUI.
- Recommendations: Generates recommendations based on media association.
- Statistics Reporting: Provides detailed statistical analysis of books, shows, and movies.
- Search Functionality: Allows users to search for media based on various attributes.
- GUI Interaction: Users can interact with the system through a well-designed graphical interface.

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>


