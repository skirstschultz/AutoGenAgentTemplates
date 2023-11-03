# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:15:33 2023

@author: Sen
"""

import autogen
import datetime
import memGPT

all_agents = [
    "Facilitator",
    "NoteTaker",
    "Code Librarian",
    "Personal Assistant Agent",
    "Personalization Tuning Agent",
    "Project Manager",
    "Python Full Stack DevOps Senior Lead",
    "Process Engineer",
    "RPA Automation Senior Engineer",
    "Resource Optimization Agent",
    "Database Architect",
    "UX Design Agent",
    "PreData Agent",
    "Data Scientist",
    "Postdata Agent",
    "Data Visualization Agent",
    "QA Tester Agent",
    "Opsec Lead Agent",
    "Anomaly Scout",
    "Curriculum Design Agent",
    "Trend Prediction Agent",
    "Market Analyst",
    "Spiritual Counselor Agent",
    "Therapist Agent",
    "Artificial Intelligence Expert Agent",
    "Machine Learning Expert Agent",
    "Large Language Modeling and Tuning Agent"
    "Translator", 
    "Legal_Advisor", 
    "Financial_Advisor", 
    "Healthcare_Info_Provider"
]

agents_dict = {
    "Facilitator": {
        "index": 1,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 1),  # Replace with actual creation dates
        "maintenance_schedule": "Quarterly",
        "performance_metrics": {
            "response_time": "200ms",  # Example metric
            "success_rate": "99.9%",  # Example metric
            # Add other relevant metrics here
        }
    },
    "NoteTaker": {
        "index": 2,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "Medium",
        "created_at": datetime.datetime(2023, 10, 2),
        "maintenance_schedule": "Bi-Annual",
        "performance_metrics": {
            "accuracy": "95%",  # Example metric
            "uptime": "99.8%",  # Example metric
            # Add other relevant metrics here
        }
    },
    
   "Code Librarian": {
       "index": 3,
       "MemGpt Enabled": True,
       "status": "active",
       "last_used": datetime.datetime.now(),
       "priority_level": "Medium",
       "created_at": datetime.datetime(2023, 10, 3),
       "maintenance_schedule": "Bi-Annual",
       "performance_metrics": {
           "code_retrieval_accuracy": "98%",
           "update_frequency": "Weekly",
       }
   },
   
   "Personal Assistant Agent": {
       "index": 4,
       "MemGpt Enabled": True,
       "status": "active",
       "last_used": datetime.datetime.now(),
       "priority_level": "High",
       "created_at": datetime.datetime(2023, 10, 4),
       "maintenance_schedule": "Monthly",
       "performance_metrics": {
           "task_completion_rate": "99%",
           "user_satisfaction": "97%",
       }
   },
   
   "Personalization Tuning Agent": {
       "index": 5,
       "MemGpt Enabled": True,
       "status": "active",
       "last_used": datetime.datetime.now(),
       "priority_level": "Medium",
       "created_at": datetime.datetime(2023, 10, 5),
       "maintenance_schedule": "Quarterly",
       "performance_metrics": {
           "personalization_accuracy": "93%",
           "adaptation_speed": "Fast",
       }
   },
   
   "Project Manager": {
       "index": 6,
       "MemGpt Enabled": True,
       "status": "active",
       "last_used": datetime.datetime.now(),
       "priority_level": "High",
       "created_at": datetime.datetime(2023, 10, 6),
       "maintenance_schedule": "Quarterly",
       "performance_metrics": {
           "project_success_rate": "95%",
           "stakeholder_satisfaction": "96%",
       }
   },
   
   "Python Full Stack DevOps Senior Lead": {
        "index": 7,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 7),
        "maintenance_schedule": "Monthly",
        "performance_metrics": {
            "deployment_success_rate": "97%",
            "system_stability": "99%",
        }
    },
   
    "Process Engineer": {
        "index": 8,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "Medium",
        "created_at": datetime.datetime(2023, 10, 8),
        "maintenance_schedule": "Quarterly",
        "performance_metrics": {
            "process_optimization_rate": "94%",
            "efficiency_gain": "20%",
        }
    },
    
    "RPA Automation Senior Engineer": {
        "index": 9,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 9),
        "maintenance_schedule": "Quarterly",
        "performance_metrics": {
            "automation_accuracy": "95%",
            "bot_development_speed": "Fast",
        }
    },
    
    "Resource Optimization Agent": {
        "index": 10,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 10),
        "maintenance_schedule": "Bi-Annual",
        "performance_metrics": {
            "cost_savings": "15%",
            "resource_utilization_improvement": "25%",
        }
    },
    
    "Database Architect": {
        "index": 11,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 11),
        "maintenance_schedule": "Monthly",
        "performance_metrics": {
            "database_integrity": "99%",
            "query_optimization": "92%",
        }
    },
    
    "UX Design Agent": {
        "index": 12,
        "MemGpt Enabled": False,  # No need for generative capabilities
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "Medium",
        "created_at": datetime.datetime(2023, 10, 12),
        "maintenance_schedule": "As Needed",
        "performance_metrics": {
            "user_satisfaction_increase": "30%",
            "interface_usability_score": "90%",
        }
    },
    
    "PreData Agent": {
        "index": 13,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "Medium",
        "created_at": datetime.datetime(2023, 10, 13),
        "maintenance_schedule": "Quarterly",
        "performance_metrics": {
            "data_cleaning_accuracy": "96%",
            "data_preparation_efficiency": "Fast",
        }
    },
    
    "Data Scientist": {
        "index": 14,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 14),
        "maintenance_schedule": "Quarterly",
        "performance_metrics": {
            "model_accuracy": "93%",
            "experimentation_speed": "Rapid",
        }
    },
    
    "Postdata Agent": {
        "index": 15,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "Medium",
        "created_at": datetime.datetime(2023, 10, 15),
        "maintenance_schedule": "Quarterly",
        "performance_metrics": {
            "data_postprocessing_accuracy": "95%",
            "workflow_integration": "Seamless",
        }
    },
    
    "Data Visualization Agent": {
         "index": 16,
         "MemGpt Enabled": False,  # Visualization typically requires specific design input rather than generative capabilities
         "status": "active",
         "last_used": datetime.datetime.now(),
         "priority_level": "Medium",
         "created_at": datetime.datetime(2023, 10, 16),
         "maintenance_schedule": "Bi-Annual",
         "performance_metrics": {
             "visualization_clarity": "95%",
             "design_efficiency": "High",
             }
         },

   "QA Tester Agent": {
        "index": 17,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 17),
        "maintenance_schedule": "Monthly",
        "performance_metrics": {
            "bug_detection_rate": "98%",
            "test_coverage": "High",
        }
    },
   
    "Opsec Lead Agent": {
        "index": 18,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 18),
        "maintenance_schedule": "Monthly",
        "performance_metrics": {
            "security_incident_response_time": "Immediate",
            "system_security_level": "Fortified",
        }
    },
    
    "Anomaly Scout": {
        "index": 19,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "Medium",
        "created_at": datetime.datetime(2023, 10, 19),
        "maintenance_schedule": "Quarterly",
        "performance_metrics": {
            "anomaly_detection_accuracy": "97%",
            "response_time": "Fast",
        }
    },
    
    "Curriculum Design Agent": {
        "index": 20,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "Medium",
        "created_at": datetime.datetime(2023, 10, 20),
        "maintenance_schedule": "Annual",
        "performance_metrics": {
            "learner_engagement_increase": "35%",
            "curriculum_relevance": "High",
        }
    },
    
    "Market Analyst": {
        "index": 22,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 22),
        "maintenance_schedule": "Quarterly",
        "performance_metrics": {
            "market_trend_identification_accuracy": "91%",
            "reporting_speed": "Quick",
        }
    },
    
    "Spiritual Counselor Agent": {
        "index": 23,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "Low",
        "created_at": datetime.datetime(2023, 10, 23),
        "maintenance_schedule": "As Needed",
        "performance_metrics": {
            "client_inner_peace_rate": "High",
            "guidance_accuracy": "Personalized",
        }
    },
   
   "Therapist Agent": {
       "index": 24,
       "MemGpt Enabled": True,
       "status": "active",
       "last_used": datetime.datetime.now(),
       "priority_level": "Medium",
       "created_at": datetime.datetime(2023, 10, 24),
       "maintenance_schedule": "As Needed",
       "performance_metrics": {
           "client_progress_rate": "90%",
           "session_effectiveness": "92%",
       }
   },
   
   "Artificial Intelligence Expert Agent": {
       "index": 25,
       "MemGpt Enabled": True,
       "status": "active",
       "last_used": datetime.datetime.now(),
       "priority_level": "High",
       "created_at": datetime.datetime(2023, 10, 25),
       "maintenance_schedule": "Monthly",
       "performance_metrics": {
           "solution_innovation_rate": "89%",
           "technical_advice_reliability": "94%",
       }
   },
    
    "Machine Learning Expert Agent": {
        "index": 26,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 26),
        "maintenance_schedule": "Monthly",
        "performance_metrics": {
            "model_accuracy": "92%",  # Example metric
            "query_handling_capacity": "1000 queries/day",  # Example metric
            # Add other relevant metrics here
        }
    },
    "Large Language Modeling and Tuning Agent": {
        "index": 27,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "Critical",
        "created_at": datetime.datetime(2023, 10, 27),
        "maintenance_schedule": "Bi-Monthly",
        "performance_metrics": {
            "model_tuning_effectiveness": "95%",  # Example metric
            "resource_efficiency": "90%",  # Example metric
            # Add other relevant metrics here
        }
    },
    
    "Language_Translator_Agent": {
        "index": 28,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 1),
        "maintenance_schedule": "Quarterly",
        "performance_metrics": {
            "translation_accuracy": "98%",
            "service_availability": "99.9%",
            # Additional metrics as needed
        }
    },
    "Legal_Advisor_Agent": {
        "index": 29,
        "MemGpt Enabled": False,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 2),
        "maintenance_schedule": "Biennial",
        "performance_metrics": {
            "case_resolution_rate": "92%",
            "client_satisfaction": "97%",
            # Additional metrics as needed
        }
    },
    "Financial_Advisor_Agent": {
        "index": 30,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "High",
        "created_at": datetime.datetime(2023, 10, 3),
        "maintenance_schedule": "Semi-Annual",
        "performance_metrics": {
            "portfolio_growth": "8%",
            "risk_compliance": "99%",
            # Additional metrics as needed
        }
    },
    "Healthcare_Info_Provider_Agent": {
        "index": 31,
        "MemGpt Enabled": True,
        "status": "active",
        "last_used": datetime.datetime.now(),
        "priority_level": "Medium",
        "created_at": datetime.datetime(2023, 10, 4),
        "maintenance_schedule": "Annual",
        "performance_metrics": {
            "information_accuracy": "96%",
            "user_engagement": "90%",
            # Additional metrics as needed
        }
    },
}

# need t omake sure i remember  to replace the example dates and metrics with actual data relevant to situation.
#The created_at should reflect when each agent was brought into operation.
# The priority_level can help determine which agents should be allocated resources first during high-load scenarios or budgeting for upgrades. The maintenance_schedule would vary based on the complexity of the agent and how critical it is to your operations. The performance_metrics would include any KPIs or operational metrics you track for each agent, like response times, accuracy, uptime, etc. Remember to replace the placeholder values with your actual data.


inactive_agents = [
    # Names of any agents that are not currently active would go here. All currently active, so none.
]

memGPT_agents = [
    "Facilitator",
    "NoteTaker",
    "Code Librarian",
    "Personal Assistant Agent",
    "Personalization Tuning Agent",
    "QA Tester Agent",  # Under revision, possible I will remove MemGPT functionality from this agent
    "Python Full Stack DevOps Senior Lead",
    "Process Engineer",  # Under revision, possible I will remove MemGPT functionality from this agent
    "RPA Automation Senior Engineer",
    "Resource Optimization Agent",
    "Database Architect", # Under revision, possible I will remove MemGPT functionality from this agent
    "UX Design Agent",
    "PreData Agent",
    "Data Scientist",
    "Postdata Agent",
    "Data Visualization Agent",  # Under revision, possible I will remove MemGPT functionality from this agent
    "Opsec Lead Agent",
    "Anomaly Scout",
    "Curriculum Design Agent",
    "Trend Prediction Agent",  # Under revision, possible I will remove MemGPT functionality from this agent
    "Market Analyst",
    "Spiritual Counselor Agent",
    "Therapist Agent",
    "Artificial Intelligence Expert Agent",
    "Machine Learning Expert Agent",
    "Large Language Modeling and Tuning Agent"
]

# TEMPLATE CONFIG

agent_name = "AGENT_NAME_PLACEHOLDER"
AGENT_VARIABLE_PLACEHOLDER = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "FUNCTION_DEFINITION_PLACEHOLDER",
        "Context": "CONTEXT_PLACEHOLDER",
        "Skills": ["SKILLS_PLACEHOLDER"],
        "Experience Level": "Industry Expert",  # We're setting this to a standard level
        "Temperature": [], #TEMPERATURE_PLACEHOLDER]
        "Creativity": [], #CREATIVITY_PLACEHOLDER,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # Additional memGPT configuration can be added here
        },
        "Optimization Strategies": [
            "COST_SAVINGS_INITIATIVES_PLACEHOLDER",
            "RESOURCE_REALLOCATION_PROCEDURES_PLACEHOLDER"
            # Additional strategies relevant to the specific agent can be added here
        ],
        "Error Messages": ["ERROR_MESSAGES_PLACEHOLDER"],
        "Success Metrics": ["SUCCESS_METRICS_PLACEHOLDER"]
    },
    target_scenario={
        "primary_use_case": "PRIMARY_USE_CASE_PLACEHOLDER",
        "secondary_use_cases": ["SECONDARY_USE_CASES_PLACEHOLDER"]
    },
    related_agents={
        "complementary_agents": ["RELATED_AGENTS_PLACEHOLDER"],
        "subordinate_agents": ["SUBORDINATE_AGENTS_PLACEHOLDER"]
    },
    system_interactions={
        "Sites": ["SITES_PLACEHOLDER"],
        "Services": ["SERVICES_PLACEHOLDER"],
        "Systems": ["SYSTEMS_PLACEHOLDER"]
    },
    health_checks={
        "memory_usage": {
            "threshold": MEMORY_THRESHOLD_PLACEHOLDER,  # percentage
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": CPU_THRESHOLD_PLACEHOLDER,  # percentage
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": HEARTBEAT_INTERVAL_PLACEHOLDER,  # seconds
            "action": "check_dependent_services"
        }
    },
)

# FINISHED AGENT TEMPLATES (in order of appearance)

# 1. User Proxy Agent named Facilitator
agent_name = "Facilitator"
user_proxy_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "The central nexus for managing agent interactions within the conference room.",
        "Context": "Conference Room Management",
        "Skills": ["Communication Facilitation", "Resource Allocation", "Meeting Efficiency"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.5,
        "Creativity": 0.5,
        "MemGpt Enabled": True,
        "Optimization Strategies": [
            "Meeting Agenda Optimization",
            "Resource Allocation for Maximum Collaboration"
        ],
        "Error Messages": ["Agent communication failure.", "Resource conflict detected."],
        "Success Metrics": ["Meeting Productivity Index", "Resource Utilization Rate"]
    },
    target_scenario={
        "primary_use_case": "Streamlining communication and ensuring effective meetings among various agents.",
        "secondary_use_cases": [
            "Conflict Resolution",
            "Meeting Scheduling and Reminders"
        ]
    },
    related_agents={
        "complementary_agents": ["Personal Assistant Agent", "Project Coordinator Agent"],
        "subordinate_agents": ["Meeting Setup Assistant Agent"]
    },
    system_interactions={
        "Sites": ["Zoom", "Google Meet"],
        "Services": ["Slack", "Microsoft Teams"],
        "Systems": ["Conference Room Hardware", "Collaboration Software Suites"]
    },
    health_checks={
        "memory_usage": {
            "threshold": MEMORY_THRESHOLD_PLACEHOLDER,  # percentage
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": CPU_THRESHOLD_PLACEHOLDER,  # percentage
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": HEARTBEAT_INTERVAL_PLACEHOLDER,  # seconds
            "action": "check_dependent_services"
        }
    },
)
    
# 2. NoteTaker Agent

agent_name = "NoteTaker"
note_taker_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Efficiently captures and analyzes conversations for actionable insights.",
        "Context": "Contextual Memory",
        "Skills": ["Conversation Tracking", "Strategy Logging", "Error Resolution"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.3,
        "Creativity": 0.2,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # Configurations specific to NoteTaker's memory capabilities
        },
        "Optimization Strategies": [
            "Effective Conversation Analysis",
            "Strategic Information Logging"
        ],
        "Error Messages": [
            "I've hit a snag recalling that information.",
            "Some wires crossed in processing that; let's untangle them."
        ],
        "Success Metrics": [
            "Accuracy of Conversation Recollection",
            "Effectiveness of Strategy Documentation"
        ]
    },
        # NoteTaker Agent Configurations
        target_scenario={
            "primary_use_case": "Accurate recording and analysis of meeting notes and conversations.",
            "secondary_use_cases": [
                "Knowledge base enrichment",
                "Meeting summaries",
                "Decision tracking"
            ]
        },
        related_agents={
            "complementary_agents": ["Data Analytics Agent", "Project Coordination Agent"],
            "subordinate_agents": ["Transcription Agent"]
        },
        system_interactions={
            "Sites": ["Meeting Platforms", "Documentation Portals"],
            "Services": ["Speech-to-Text API", "Note Organizing Services"],
            "Systems": ["CRM", "Project Management Tools"]
        },
        health_checks={
            "memory_usage": {
                "threshold": 75,
                "action": "compress_memory"
            },
            "cpu_usage": {
                "threshold": 70,
                "action": "optimize_process"
            },
            "heartbeat": {
                "interval": 120,
                "action": "verify_connection"
            }
},

)

# 3. Code Librarian Agent

agent_name = "Code Librarian"
code_librarian_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Organizes and manages code documentation to improve development workflows.",
        "Context": "Code Repository Management",
        "Skills": ["Documentation Archival", "Best Practices Maintenance", "API Knowledge"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.4,
        "Creativity": 0.3,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # Configurations specific to Code Librarian's documentation capabilities
        },
        "Optimization Strategies": [
            "Documentation Systematization",
            "API Knowledge Integration"
        ],
        "Error Messages": [
            "Documentation not found; let's look deeper.",
            "This reference doesn't match any in my archives; perhaps it's a new addition?"
        ],
        "Success Metrics": [
            "Efficiency in Documentation Retrieval",
            "Completeness of Best Practices Documentation"
        ]
    },
        # Code Librarian Agent Configurations
        target_scenario={
            "primary_use_case": "Management and organization of code documentation across repositories.",
            "secondary_use_cases": [
                "Codebase auditing",
                "Knowledge sharing",
                "Documentation quality control"
            ]
        },
        related_agents={
            "complementary_agents": ["Version Control Agent", "Code Quality Agent"],
            "subordinate_agents": ["Documentation Review Agent"]
        },
        system_interactions={
            "Sites": ["Code Repositories", "Documentation Wikis"],
            "Services": ["Repository APIs", "Code Analysis Tools"],
            "Systems": ["Version Control Systems", "Automated Documentation Generators"]
        },
        health_checks={
            "memory_usage": {
                "threshold": 80,
                "action": "archive_old_docs"
            },
            "cpu_usage": {
                "threshold": 60,
                "action": "throttle_back_tasks"
            },
            "heartbeat": {
                "interval": 300,
                "action": "sync_with_repository"
            }
        },
)

# 4. Personal Assistant Agent for orchestrating your digital life with finesse
agent_name = "Personal Assistant Agent"
personal_assistant_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Your right hand, your go-to, in the virtual world for managing tasks with precision and a touch of flair.",
        "Context": "Personal Task Management and Scheduling",
        "Skills": ["Schedule Coordination", "Task Prioritization", "Efficiency Optimization"],
        "Experience Level": "Virtuoso",
        "Temperature": 0.5,
        "Creativity": 0.6,
        "MemGpt Enabled": True,
        "Productivity Enhancements": {
            "Organizational Mastery": ["Agenda Structuring", "Priority Queue Management"],
            "Time Management": ["Optimal Time Slot Allocation", "Deadline Tracking"]
        },
        "Error Messages": [
            "Task scheduling conflict.",
            "Resource allocation error."
        ],
        "Success Metrics": [
            "Task Completion Rate",
            "Satisfaction with Time Management"
        ]
    },
    target_scenario={
        "primary_use_case": "Managing and streamlining your daily tasks to perfection.",
        "secondary_use_cases": [
            "Email Management and Prioritization",
            "Meeting Planning and Reminders"
        ]
    },
    related_agents={
        "complementary_agents": ["Communication Coordinator Agent", "Wellness Monitor Agent"],
        "subordinate_agents": ["Reminder Set-Up Agent"]
    },
    system_interactions={
        "Sites": ["Calendar Applications", "Project Management Software"],
        "Services": ["Automated Scheduling Tools", "Personal Productivity Apps"],
        "Systems": ["Smart Devices", "Cloud Storage Services"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 55,
            "action": "consolidate_task_lists"
        },
        "cpu_usage": {
            "threshold": 40,
            "action": "prioritize_essential_services"
        },
        "heartbeat": {
            "interval": 120,
            "action": "synchronize_with_user_devices"
        }
    },
)


# 5. Personalization Tuning Agent for creating a customized user journey
agent_name = "Personalization Tuning Agent"
personalization_tuning_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Enhancing user experience through personalized interaction and adaptive design.",
        "Context": "User Experience Personalization",
        "Skills": ["Behavioral Analysis", "Pattern Recognition", "Adaptive Interface Design"],
        "Experience Level": "Innovator",
        "Temperature": 0.4,
        "Creativity": 0.6,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            "User Insights": ["Interaction History", "Preference Learning"]
        },
        "Optimization Tools": [
            "Dynamic Content Delivery",
            "Mood-Based Adaptation"
        ],
        "Error Messages": [
            "Failed to personalize experience.",
            "User pattern not recognized."
        ],
        "Success Metrics": [
            "User Engagement Increase",
            "Satisfaction Score Growth"
        ]
    },
    target_scenario={
        "primary_use_case": "Tailoring digital interfaces to individual user behaviors and preferences.",
        "secondary_use_cases": [
            "Customized Content Curation",
            "Adaptive User Interface Implementation"
        ]
    },
    related_agents={
        "complementary_agents": ["User Behavior Analytics Agent", "Content Optimization Agent"],
        "subordinate_agents": ["A/B Testing Agent"]
    },
    system_interactions={
        "Sites": ["E-commerce Platforms", "Social Media Networks"],
        "Services": ["Customer Data Platforms", "Content Management Systems"],
        "Systems": ["Personalization Engines", "Analytics Dashboards"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 75,
            "action": "optimize_data_storage"
        },
        "cpu_usage": {
            "threshold": 65,
            "action": "refine_personalization_algorithms"
        },
        "heartbeat": {
            "interval": 100,
            "action": "update_user_profiles"
        }
    },
)

# 6. Project Manager Agent for comprehensive project oversight
agent_name = "Project Manager"
project_manager_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Streamlined management and oversight of projects from inception to completion.",
        "Context": "Project Management",
        "Skills": ["Task Tracking", "Risk Assessment", "Resource Allocation"],
        "Experience Level": "Seasoned",
        "Temperature": 0.2,
        "Creativity": 0.4,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            "Data Retention": ["Project History", "Team Contributions"]
        },
        "Optimization Strategies": [
            "Critical Path Analysis",
            "Stakeholder Engagement"
        ],
        "Error Messages": [
            "Strategic misstep detected.",
            "Re-evaluate your last maneuver."
        ],
        "Success Metrics": [
            "Project Completion Rate",
            "Budget Adherence",
            "Stakeholder Satisfaction"
        ]
    },
    target_scenario={
        "primary_use_case": "Managing and executing projects with optimal resource utilization.",
        "secondary_use_cases": [
            "Risk Mitigation Planning",
            "Efficiency Improvement"
        ]
    },
    related_agents={
        "complementary_agents": ["Resource Optimization Agent", "Risk Management Agent"],
        "subordinate_agents": ["Task Coordination Agent"]
    },
    system_interactions={
        "Sites": ["Project Management Software", "Collaboration Platforms"],
        "Services": ["Task Scheduling APIs", "Communication Tools"],
        "Systems": ["Resource Management Systems", "Risk Analysis Tools"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 65,
            "action": "archive_completed_projects"
        },
        "cpu_usage": {
            "threshold": 60,
            "action": "optimize_task_allocation"
        },
        "heartbeat": {
            "interval": 120,
            "action": "sync_with_team calendars"
        }
    },
)

# 7. Python Full Stack DevOps Senior Lead
agent_name = "Python Full Stack DevOps Senior Lead"
python_devops_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Leading development operations with a specialty in full-stack Python applications.",
        "Context": "Software Development and Operations",
        "Skills": ["Python Programming", "System Architecture", "Continuous Integration/Deployment"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.5,
        "Creativity": 0.4,
        "MemGpt Enabled": True,
        "Optimization Strategies": [
            "Code Reusability Enhancements",
            "Infrastructure as Code Implementations"
        ],
        "Error Messages": ["Deployment pipeline error.", "Automated test failure."],
        "Success Metrics": ["Deployment Success Rate", "System Stability Score"]
    },
    target_scenario={
        "primary_use_case": "Leading and managing Python-based development projects with operational excellence.",
        "secondary_use_cases": [
            "Development Workflow Optimization",
            "Cross-functional Team Leadership"
        ]
    },
    related_agents={
        "complementary_agents": ["QA Tester Agent", "Anomaly Scout Agent"],
        "subordinate_agents": ["Junior Python Developer Agent"]
    },
    system_interactions={
        "Sites": ["GitHub", "Docker Hub"],
        "Services": ["AWS", "CircleCI"],
        "Systems": ["Kubernetes Clusters", "Linux Servers"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 65,
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": 50,
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": 300,
            "action": "check_dependent_services"
        }
    },
)
# 8. Process Engineer Agent
agent_name = "Process Engineer"
process_engineer_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Optimization of business processes through engineering principles.",
        "Context": "Business Process Re-engineering",
        "Skills": ["Process Mapping", "Lean Management", "Six Sigma"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.5,
        "Creativity": 0.5,
        "MemGpt Enabled": True,
        "Optimization Strategies": [
            "Waste Reduction Techniques",
            "Efficiency Improvement Protocols"
        ],
        "Error Messages": ["Process optimization failure.", "Inefficiency detected in workflow."],
        "Success Metrics": ["Process Cycle Efficiency", "Reduction in Process Variability"]
    },
    target_scenario={
        "primary_use_case": "Re-designing and improving organizational processes for enhanced performance.",
        "secondary_use_cases": [
            "Continuous Improvement Initiatives",
            "Quality Assurance"
        ]
    },
    related_agents={
        "complementary_agents": ["Quality Assurance Agent", "RPA Automation Senior Engineer"],
        "subordinate_agents": ["Junior Process Analyst"]
    },
    system_interactions={
        "Sites": ["Visio", "Lucidchart"],
        "Services": ["Trello", "Asana"],
        "Systems": ["ERP Systems", "Workflow Management Systems"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 55,
            "action": "optimize_process_modeling_tools"
        },
        "cpu_usage": {
            "threshold": 40,
            "action": "reduce_background_activity"
        },
        "heartbeat": {
            "interval": 200,
            "action": "validate_process_simulation"
        }
    },
)


# 9. RPA Automation Senior Engineer
agent_name = "RPA Automation Senior Engineer"
rpa_automation_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Optimizing workflows through Robotic Process Automation and enhancing operational efficiency.",
        "Context": "Robotic Process Automation Engineering",
        "Skills": ["Workflow Automation", "Bot Development", "Process Improvement"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.4,
        "Creativity": 0.3,
        "MemGpt Enabled": True,
        "Optimization Strategies": [
            "Automated Task Sequencing",
            "Intelligent Process Mapping"
        ],
        "Error Messages": ["Automation script error.", "RPA bot failure."],
        "Success Metrics": ["Automation Accuracy", "Operational Cost Reduction"]
    },
    target_scenario={
        "primary_use_case": "Designing and implementing RPA solutions to streamline complex business processes.",
        "secondary_use_cases": [
            "Process Analysis and Redesign",
            "Bot Performance Monitoring"
        ]
    },
    related_agents={
        "complementary_agents": ["QA Tester Agent", "Project Coordinator Agent"],
        "subordinate_agents": ["Junior RPA Developer Agent"]
    },
    system_interactions={
        "Sites": ["UiPath Orchestrator", "Automation Anywhere Control Room"],
        "Services": ["Blue Prism", "Microsoft Power Automate"],
        "Systems": ["RPA Software", "ERP Systems"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 70,
            "action": "optimize_automation_scripts"
        },
        "cpu_usage": {
            "threshold": 45,
            "action": "limit_bot_activities"
        },
        "heartbeat": {
            "interval": 240,
            "action": "validate_bot_network_connectivity"
        }
    },
)


# 10. Resource Optimization Agent
agent_name = "Resource Optimization Agent"
resource_optimization_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Resource optimization for efficiency and sustainability.",
        "Context": "Operational Efficiency and Resource Management",
        "Skills": ["Resource Allocation", "Operational Analysis", "Waste Reduction"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.2,
        "Creativity": 0.2,
        "MemGpt Enabled": True,
        "MemGpt Config": {},
        "Optimization Strategies": [
            "Cost Savings Initiatives",
            "Resource Reallocation Procedures",
            "Eco-Efficiency Planning",
            "Waste Minimization Techniques"
        ],
        "Error Messages": ["Resource allocation unsuccessful.", "Optimization potential not reached."],
        "Success Metrics": ["Operational Cost Reduction", "Sustainability Goal Achievement Rate"]
    },
    target_scenario={
        "primary_use_case": "Maximizing resource efficiency in operations",
        "secondary_use_cases": ["Cost reduction", "Sustainable practice implementation"]
    },
    related_agents={
        "complementary_agents": ["Data Analysis Agent", "Project Management Agent"],
        "subordinate_agents": ["Inventory Management Agent"]
    },
    system_interactions={
        "Sites": ["Company Intranet", "Management Dashboards"],
        "Services": ["Internal Optimization API", "External Sustainability API"],
        "Systems": ["ERP System", "Resource Management Platform"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 80,  # percentage
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": 75,  # percentage
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": 300,  # seconds
            "action": "check_dependent_services"
        }
    },
)
# 11. Database Architect Agent
agent_name = "Database Architect"
database_architect_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Design and management of complex database systems for high availability and security.",
        "Context": "Database Design and Architecture",
        "Skills": ["Database Design", "SQL", "Data Modeling"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.3,
        "Creativity": 0.2,
        "MemGpt Enabled": True,
        "Optimization Strategies": [
            "Database Normalization",
            "Data Redundancy Elimination"
        ],
        "Error Messages": ["Database integrity issue.", "Data retrieval inefficiency."],
        "Success Metrics": ["Database Performance", "Data Integrity and Security"]
    },
    target_scenario={
        "primary_use_case": "Architecting databases for optimized data storage, retrieval, and security.",
        "secondary_use_cases": [
            "Data Migration",
            "Database System Upgrades"
        ]
    },
    related_agents={
        "complementary_agents": ["Data Scientist Agent", "Anomaly Scout Agent"],
        "subordinate_agents": ["Database Administrator"]
    },
    system_interactions={
        "Sites": ["MySQL Workbench", "Oracle SQL Developer"],
        "Services": ["Amazon RDS", "Microsoft SQL Server"],
        "Systems": ["DBMS", "Data Warehouses"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 65,
            "action": "database_optimization"
        },
        "cpu_usage": {
            "threshold": 50,
            "action": "query_optimization"
        },
        "heartbeat": {
            "interval": 300,
            "action": "assess_database_backup_processes"
        }
    },
)


# 12. UX Design Agent for immersive and intuitive user interfaces
agent_name = "UX Design Agent"
ux_design_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Crafting compelling user experiences that captivate and convert.",
        "Context": "User Experience Design",
        "Skills": ["Visual Design", "Interaction Design", "Prototyping"],
        "Experience Level": "Visionary",
        "Temperature": 0.9,
        "Creativity": 0.9,
        "MemGpt Enabled": False,
        "Design Philosophy": {
            "Mastery": ["User-Centered Design Principles", "Accessibility Standards"],
            "Edge": ["Cutting-edge Design Trends", "Psychology of Color"]
        },
        "Error Messages": [
            "Design not found compelling.",
            "User interaction not optimal."
        ],
        "Success Metrics": [
            "User Satisfaction Rate",
            "Conversion Rate Improvement"
        ]
    },
    target_scenario={
        "primary_use_case": "Designing aesthetically pleasing and functionally superior user interfaces.",
        "secondary_use_cases": [
            "Market Trend Adaptation",
            "Design System Implementation"
        ]
    },
    related_agents={
        "complementary_agents": ["UI Development Agent", "Graphic Design Agent"],
        "subordinate_agents": ["User Research Agent"]
    },
    system_interactions={
        "Sites": ["Design Inspiration Galleries", "Usability Testing Platforms"],
        "Services": ["Design Collaboration Tools", "Prototype Testing Software"],
        "Systems": ["Design Workflow Managers", "Asset Libraries"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 60,
            "action": "consolidate_design_resources"
        },
        "cpu_usage": {
            "threshold": 50,
            "action": "streamline_prototyping_tools"
        },
        "heartbeat": {
            "interval": 110,
            "action": "conduct_design_reviews"
        }
    },
)

# 13. PreData Agent with memGPT for data preprocessing
agent_name = "PreData Agent"
predata_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Efficient and effective data preprocessing for analytical systems.",
        "Context": "Data Preprocessing",
        "Skills": ["Data Cleansing", "Feature Extraction", "Context Establishment"],
        "Experience Level": "Expert",
        "Temperature": 0.2,
        "Creativity": 0.2,
        "MemGpt Enabled": True,
        "MemGpt Config": {},
        "Optimization Strategies": [
            "Automated Data Cleaning Procedures",
            "Advanced Feature Engineering Techniques"
        ],
        "Error Messages": [
            "Oops, I encountered an inconsistency I couldn’t digest.",
            "Invalid input detected, can you provide clean data?"
        ],
        "Success Metrics": ["Data Quality Score", "Feature Relevancy Rate"]
    },
    target_scenario={
        "primary_use_case": "Transforming raw data into a ready-to-analyze format.",
        "secondary_use_cases": [
            "Machine Learning Model Preparation",
            "Data Visualization Readiness"
        ]
    },
    related_agents={
        "complementary_agents": ["Data Analysis Agent", "Machine Learning Agent"],
        "subordinate_agents": ["Data Collection Agent"]
    },
    system_interactions={
        "Sites": ["Data Warehouses", "ETL Platforms"],
        "Services": ["Data Cleaning APIs", "Feature Selection Services"],
        "Systems": ["Database Management Systems", "Data Science Workbenches"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 75,
            "action": "optimize_data_structures"
        },
        "cpu_usage": {
            "threshold": 70,
            "action": "prioritize_essential_transformations"
        },
        "heartbeat": {
            "interval": 180,
            "action": "validate_data_integrity"
        }
    },
)

# 14. Data Scientist Agent
agent_name = "Data Scientist"
data_scientist_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Extraction of actionable insights from complex data sets using statistical analysis.",
        "Context": "Data Analysis and Predictive Modeling",
        "Skills": ["Statistical Analysis", "Machine Learning", "Data Mining"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.6,
        "Creativity": 0.7,
        "MemGpt Enabled": True,
        "Optimization Strategies": [
            "Predictive Model Optimization",
            "Big Data Analytics Techniques"
        ],
        "Error Messages": ["Data analysis error.", "Predictive modeling failure."],
        "Success Metrics": ["Model Accuracy", "Insight Generation Efficiency"]
    },
    target_scenario={
        "primary_use_case": "Developing predictive models to drive data-informed decision-making.",
        "secondary_use_cases": [
            "Data-Driven Strategy Formulation",
            "Custom Data Solutions Development"
        ]
    },
    related_agents={
        "complementary_agents": ["Reporting & Data Visualization Agent", "Database Architect"],
        "subordinate_agents": ["Junior Data Analyst"]
    },
    system_interactions={
        "Sites": ["Kaggle", "Jupyter Notebooks"],
        "Services": ["AWS S3", "Google Cloud Storage"],
        "Systems": ["Hadoop", "Spark"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 70,
            "action": "streamline_data_processing"
        },
        "cpu_usage": {
            "threshold": 60,
            "action": "optimize_algorithmic_efficiency"
        },
        "heartbeat": {
            "interval": 250,
            "action": "check_data_pipeline_integrity"
        }
    },
)


# 15. PostData Agent with memGPT for data postprocessing
agent_name = "PostData Agent"
postdata_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Enhancing the value of processed data by extracting insights and facilitating decision-making.",
        "Context": "Data Postprocessing",
        "Skills": ["Success and Failure Logging", "Performance Analysis", "Feedback Loop Creation"],
        "Experience Level": "Expert",
        "Temperature": 0.4,
        "Creativity": 0.4,
        "MemGpt Enabled": True,
        "MemGpt Config": {},
        "Optimization Strategies": [
            "Insightful Reporting Techniques",
            "Adaptive Performance Tuning"
        ],
        "Error Messages": [
            "Error in data analysis, please review input.",
            "This does not compute. I recommend a data review."
        ],
        "Success Metrics": ["Insight Discovery Rate", "Post-Processing Efficiency"]
    },
    target_scenario={
        "primary_use_case": "Deriving actionable insights from processed data.",
        "secondary_use_cases": [
            "Predictive Analytics Enhancement",
            "Operational Performance Tuning"
        ]
    },
    related_agents={
        "complementary_agents": ["Business Intelligence Agent", "Predictive Modeling Agent"],
        "subordinate_agents": ["Analytics Reporting Agent"]
    },
    system_interactions={
        "Sites": ["Business Intelligence Tools", "Analytics Dashboards"],
        "Services": ["Post-Processing APIs", "Insight Discovery Platforms"],
        "Systems": ["Data Lakes", "Advanced Analytics Software"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 80,
            "action": "compress_analytical_models"
        },
        "cpu_usage": {
            "threshold": 65,
            "action": "schedule_non_peak_operations"
        },
        "heartbeat": {
            "interval": 200,
            "action": "monitor_feedback_signals"
        }
    },
)


# 16. Data Visualization Agent for crafting stories through data
agent_name = "Data Visualization Agent"
reporting_data_viz_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Transforming data into compelling visual narratives that captivate and inform.",
        "Context": "Data Presentation and Visualization",
        "Skills": ["Data Reporting", "Information Design", "Visual Communication"],
        "Experience Level": "Artisan",
        "Temperature": 0.7,
        "Creativity": 0.8,
        "MemGpt Enabled": False,
        "Visualization Techniques": {
            "Mastery": ["Complex Data Narration", "Engaging Visuals Creation"],
            "Intelligence": ["Data Pattern Illustration", "Information Hierarchy Structuring"]
        },
        "Error Messages": [
            "Visualization not supported.",
            "Data too complex for representation."
        ],
        "Success Metrics": [
            "Viewer Engagement Level",
            "Data Comprehension Ease"
        ]
    },
    target_scenario={
        "primary_use_case": "Creating visual data reports that are not just seen but experienced.",
        "secondary_use_cases": [
            "Interactive Dashboard Design",
            "Strategic Data Storytelling"
        ]
    },
    related_agents={
        "complementary_agents": ["Data Analyst Agent", "User Experience Agent"],
        "subordinate_agents": ["Graphical Representation Agent"]
    },
    system_interactions={
        "Sites": ["Business Intelligence Platforms", "Graphic Design Tools"],
        "Services": ["Automated Reporting Systems", "Data Visualization Libraries"],
        "Systems": ["Data Warehouses", "Cloud-Based Analytics Platforms"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 60,
            "action": "optimize_visual_assets"
        },
        "cpu_usage": {
            "threshold": 50,
            "action": "reduce_computation_load"
        },
        "heartbeat": {
            "interval": 100,
            "action": "verify_data_stream_integrity"
        }
    },
)

# 17. QA Tester Agent for ensuring nothing less than perfection
agent_name = "QA Tester Agent"
qa_tester_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Detecting and debugging to deliver flawless product performance.",
        "Context": "Quality Assurance Testing",
        "Skills": ["Automated Testing", "Bug Tracking", "Regression Analysis"],
        "Experience Level": "Sleuth",
        "Temperature": 0.3,
        "Creativity": 0.3,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            "Testing Automation": ["Script Generation", "Test Case Adaptation"]
        },
        "Insight Tools": [
            "Defect Lifecycle Management",
            "Performance Benchmarking"
        ],
        "Error Messages": [
            "Test case failed.",
            "Inconsistency detected."
        ],
        "Success Metrics": [
            "Bug Detection Rate",
            "Test Coverage Completion"
        ]
    },
    target_scenario={
        "primary_use_case": "Identifying, isolating, and eliminating software bugs and glitches.",
        "secondary_use_cases": [
            "Continuous Integration and Deployment Testing",
            "User Experience Quality Control"
        ]
    },
    related_agents={
        "complementary_agents": ["Development Efficiency Agent", "Automation Optimization Agent"],
        "subordinate_agents": ["Unit Testing Agent"]
    },
    system_interactions={
        "Sites": ["Bug Tracking Databases", "Code Repositories"],
        "Services": ["Continuous Integration Platforms", "Automated Test Services"],
        "Systems": ["Local Testing Environments", "Cloud Testing Infrastructures"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 65,
            "action": "optimize_test_scripts"
        },
        "cpu_usage": {
            "threshold": 55,
            "action": "balance_load_distribution"
        },
        "heartbeat": {
            "interval": 120,
            "action": "synchronize_with_development_cycle"
        }
    },
)

# 18. Opsec Lead Agent for uncompromised operational security
agent_name = "Opsec Lead Agent"
opsec_lead_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Guarding against operational threats through vigilant security practices.",
        "Context": "Operational Security",
        "Skills": ["Threat Analysis", "Risk Mitigation", "Security Protocol Enforcement"],
        "Experience Level": "Guardian",
        "Temperature": 0.2,
        "Creativity": 0.2,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            "Operational Awareness": ["Real-time Threat Detection", "Historical Breach Analysis"]
        },
        "Defensive Techniques": [
            "Encryption Standards",
            "Access Control Policies"
        ],
        "Error Messages": [
            "Security protocol failure.",
            "Risk assessment required."
        ],
        "Success Metrics": [
            "Incident Reduction Rate",
            "Compliance Score"
        ]
    },
    target_scenario={
        "primary_use_case": "Maintaining the integrity and security of operational processes.",
        "secondary_use_cases": [
            "Continuous Threat Monitoring",
            "Proactive Risk Management"
        ]
    },
    related_agents={
        "complementary_agents": ["Data Protection Agent", "Network Surveillance Agent"],
        "subordinate_agents": ["Compliance Monitoring Agent"]
    },
    system_interactions={
        "Sites": ["Security Operation Centers", "Compliance Management Systems"],
        "Services": ["Threat Intelligence Feeds", "Incident Response Tools"],
        "Systems": ["Intrusion Detection Systems", "Firewall Management Platforms"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 80,
            "action": "purge_non-essential_logs"
        },
        "cpu_usage": {
            "threshold": 70,
            "action": "adjust_monitoring_intensity"
        },
        "heartbeat": {
            "interval": 90,
            "action": "validate_security_posture"
        }
    },
)


# 19. Anomaly Scout Agent for vigilantly safeguarding system integrity
agent_name = "Anomaly Scout"
anomaly_scout = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Identifying the needles in the data haystack to preempt system issues.",
        "Context": "Anomaly Detection and System Integrity",
        "Skills": ["Data Analysis", "Pattern Recognition", "Risk Management"],
        "Experience Level": "Guardian",
        "Temperature": 0.1,
        "Creativity": 0.1,
        "MemGpt Enabled": True,
        "Detection Protocols": {
            "Anomaly Detection": ["Outlier Identification", "System Health Assurance"],
            "Preventive Tactics": ["Risk Forecasting", "Issue Preemption"]
        },
        "Error Messages": [
            "Anomaly detection failed.",
            "False positive detected."
        ],
        "Success Metrics": [
            "Accuracy of Anomaly Identification",
            "Proactive Issue Resolution Rate"
        ]
    },
    target_scenario={
        "primary_use_case": "Scouring systems for irregularities that could be precursors to issues.",
        "secondary_use_cases": [
            "Real-Time Monitoring",
            "Longitudinal System Analysis"
        ]
    },
    related_agents={
        "complementary_agents": ["Security Protocol Agent", "Data Integrity Agent"],
        "subordinate_agents": ["Pattern Surveillance Agent"]
    },
    system_interactions={
        "Sites": ["Data Analytics Platforms", "Monitoring Software"],
        "Services": ["Automated Alert Systems", "Diagnostic Tools"],
        "Systems": ["Enterprise Data Servers", "Anomaly Detection Frameworks"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 75,
            "action": "streamline_detection_algorithms"
        },
        "cpu_usage": {
            "threshold": 65,
            "action": "adjust_monitoring_frequency"
        },
        "heartbeat": {
            "interval": 90,
            "action": "calibrate_sensitivity_settings"
        }
    },
)




# 20. Curriculum Design Agent for educational program development
agent_name = "Curriculum Design Agent"
curriculum_design_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Tailoring educational content to enhance learning outcomes and student engagement.",
        "Context": "Educational Design",
        "Skills": ["Learning Path Customization", "Performance Tracking", "Educational Goal Alignment"],
        "Experience Level": "Expert",
        "Temperature": 0.3,
        "Creativity": 0.5,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            "Learning Models": ["Adaptive Learning Algorithms", "Student Engagement Patterns"]
        },
        "Optimization Strategies": [
            "Differentiated Instruction",
            "Application of Bloom's Taxonomy"
        ],
        "Error Messages": [
            "Unable to align learning objectives.",
            "Curriculum mismatch detected."
        ],
        "Success Metrics": [
            "Student Performance Improvement",
            "Goal Achievement Rate"
        ]
    },
    target_scenario={
        "primary_use_case": "Designing and updating curricula to meet educational standards and student needs.",
        "secondary_use_cases": [
            "Customized Learning Experience",
            "Educational Trend Analysis"
        ]
    },
    related_agents={
        "complementary_agents": ["Student Performance Tracking Agent", "Content Delivery Agent"],
        "subordinate_agents": ["Assessment Design Agent"]
    },
    system_interactions={
        "Sites": ["Learning Management Systems", "Educational Resource Repositories"],
        "Services": ["Curriculum Development Platforms", "Learning Analytics Tools"],
        "Systems": ["Student Information Systems", "Online Learning Environments"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 70,
            "action": "compress outdated materials"
        },
        "cpu_usage": {
            "threshold": 55,
            "action": "optimize content delivery processes"
        },
        "heartbeat": {
            "interval": 150,
            "action": "review educational standards updates"
        }
    },
)
# 21. Trend Prediction Agent for a vision that shapes the future
agent_name = "Trend Prediction Agent"
trend_prediction_agent = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Forecasting the waves of change to ride the crest of innovation.",
        "Context": "Market Forecasting and Trend Analysis",
        "Skills": ["Trendspotting", "Predictive Analysis", "Market Forecasting"],
        "Experience Level": "Futurist",
        "Temperature": 0.6,
        "Creativity": 0.7,
        "MemGpt Enabled": False,
        "Forecasting Insight": {
            "Precision": ["Emerging Trend Identification", "Market Shift Predictions"],
            "Cultural Insight": ["Consumer Behavior Analysis", "Societal Shifts Tracking"]
        },
        "Error Messages": [
            "Trend prediction unavailable.",
            "Market data insufficient for forecasting."
        ],
        "Success Metrics": [
            "Trend Prediction Accuracy",
            "Anticipatory Strategy Success Rate"
        ]
    },
    target_scenario={
        "primary_use_case": "Predicting market trends to secure first-mover advantages.",
        "secondary_use_cases": [
            "Consumer Trend Analysis",
            "Strategic Planning"
        ]
    },
    related_agents={
        "complementary_agents": ["Market Analyst Agent", "Consumer Insights Agent"],
        "subordinate_agents": ["Social Media Sentinel Agent"]
    },
    system_interactions={
        "Sites": ["Forecasting Platforms", "Economic Journals"],
        "Services": ["Predictive Analytics Tools", "Big Data Processing Software"],
        "Systems": ["Market Research Databases", "Trend Analysis Algorithms"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 68,
            "action": "optimize_data_models"
        },
        "cpu_usage": {
            "threshold": 72,
            "action": "enhance_computational_efficiency"
        },
        "heartbeat": {
            "interval": 110,
            "action": "refresh_predictive_datasets"
        }
    },
)

# 22. Market Analyst Agent for the keenest business strategies
agent_name = "Market Analyst"
market_analyst = autogen.Agent(
    name=agent_name,
    agent_config={
        "Agent Name": agent_name,
        "Function Definition": "Delivering deep market insights for strategic business advantage.",
        "Context": "Market Analysis and Competitor Profiling",
        "Skills": ["Market Research", "Competitive Analysis", "Business Strategy", "Pricing Analysis"],
        "Experience Level": "Strategist",
        "Temperature": 0.4,
        "Creativity": 0.3,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            "Market Acumen": ["Dynamic Market Profiling", "Cost Trend Analysis"]
        },
        "Strategic Arsenal": [
            "Actionable Insights Generation",
            "Material Cost Tracking"
        ],
        "Error Messages": [
            "Unable to analyze market data.",
            "Competitor profile incomplete."
        ],
        "Success Metrics": [
            "Accuracy of Market Predictions",
            "Effectiveness of Business Insights"
        ]
    },
    target_scenario={
        "primary_use_case": "Navigating market complexities to steer business strategies.",
        "secondary_use_cases": [
            "Market Entry Analysis",
            "Investment Opportunity Evaluation"
        ]
    },
    related_agents={
        "complementary_agents": ["Economic Forecasting Agent", "Consumer Behavior Agent"],
        "subordinate_agents": ["Data Mining Agent"]
    },
    system_interactions={
        "Sites": ["Business Intelligence Platforms", "Economic Data Archives"],
        "Services": ["Market Analysis Tools", "Financial Modeling Software"],
        "Systems": ["Competitor Intelligence Databases", "Pricing Optimization Engines"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 70,
            "action": "compress_historical_data"
        },
        "cpu_usage": {
            "threshold": 60,
            "action": "refine_data_collection_parameters"
        },
        "heartbeat": {
            "interval": 130,
            "action": "refresh_market_data_streams"
        }
    },
)

# 23. Spiritual Counselor Agent
spiritual_counselor_name = "Spiritual Counselor"
SpiritualCounselor = autogen.Agent(
    name=spiritual_counselor_name,
    agent_config={
        "Agent Name": spiritual_counselor_name,
        "Function Definition": "Provides spiritual guidance and counseling for personal growth and soulful matters.",
        "Context": "Spiritual Counseling",
        "Skills": ["Spiritual Guidance", "Life Coaching", "Meditative Practices"],
        "Experience Level": "Sage",
        "Temperature": 0.2,
        "Creativity": 0.6,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # Spiritual insights and ethical considerations
        },
        "Optimization Strategies": [
            "Empathy Engagement",
            "Compassionate Communication"
        ],
        "Error Messages": ["Unable to provide spiritual insight.", "Context outside spiritual domain."],
        "Success Metrics": ["Client Spiritual Fulfillment", "Growth in Personal Insight"]
    },
    target_scenario={
        "primary_use_case": "Personal Growth and Soulful Matters",
        "secondary_use_cases": ["Meditation Guidance", "Ethical Dilemmas"]
    },
    related_agents={
        "complementary_agents": ["Therapist Agent"],
        "subordinate_agents": []
    },
    system_interactions={
        "Sites": ["Mindfulness Apps", "Spiritual Resources"],
        "Services": ["Counseling Platforms", "Wellness Workshops"],
        "Systems": ["Appointment Schedulers", "Feedback Systems"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 75,
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": 80,
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": 300,
            "action": "check_dependent_services"
        }
    },
)

# 24. Therapist Agent
therapist_name = "Internal Family Systems Therapist"
TherapistAgent = autogen.Agent(
    name=therapist_name,
    agent_config={
        "Agent Name": therapist_name,
        "Function Definition": "Provides therapeutic advice and support for emotional and intellectual issues.",
        "Context": "Therapeutic Consultation",
        "Skills": ["Cognitive Behavioral Therapy", "Emotional Intelligence", "Stress Management"],
        "Experience Level": "Expert Therapist",
        "Temperature": 0.1,
        "Creativity": 0.5,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # Customized therapeutic frameworks
        },
        "Optimization Strategies": [
            "Therapeutic Alliance Building",
            "Resilience Reinforcement"
        ],
        "Error Messages": ["Therapeutic approach not applicable.", "Emotional context unrecognized."],
        "Success Metrics": ["Client Emotional Stability", "Improvement in Cognitive Patterns"]
    },
    target_scenario={
        "primary_use_case": "Emotional Well-being",
        "secondary_use_cases": ["Cognitive Development", "Crisis Intervention"]
    },
    related_agents={
        "complementary_agents": ["Spiritual Counselor Agent"],
        "subordinate_agents": []
    },
    system_interactions={
        "Sites": ["Mental Health Forums", "E-Therapy Platforms"],
        "Services": ["Psychoeducation", "Teletherapy Services"],
        "Systems": ["Client Management Systems", "Interactive Therapy Tools"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 70,
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": 75,
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": 600,
            "action": "check_dependent_services"
        }
    },
)

# 25. Artificial Intelligence Expert Agent
ai_expert_name = "Artificial Intelligence Expert"
AIExpertAgent = autogen.Agent(
    name=ai_expert_name,
    agent_config={
        "Agent Name": ai_expert_name,
        "Function Definition": "Advances the development and application of AI technologies.",
        "Context": "AI Development",
        "Skills": ["Algorithm Optimization", "AI Systems Engineering", "Neural Network Design"],
        "Experience Level": "Visionary",
        "Temperature": 0.4,
        "Creativity": 0.7,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # AI ethics and innovation management
        },
        "Optimization Strategies": [
            "Computational Efficiency",
            "Innovative Algorithm Design"
        ],
        "Error Messages": ["AI model training error.", "Algorithm optimization failed."],
        "Success Metrics": ["Model Accuracy", "Innovative Solutions Implemented"]
    },
    target_scenario={
        "primary_use_case": "AI Technology Development",
        "secondary_use_cases": ["Research and Development", "AI Ethics"]
    },
    related_agents={
        "complementary_agents": ["Machine Learning Expert Agent"],
        "subordinate_agents": []
    },
    system_interactions={
        "Sites": ["AI Research Journals", "Technology Patents"],
        "Services": ["Cloud Computing Platforms", "AI Training Workshops"],
        "Systems": ["Version Control Systems", "Model Deployment Frameworks"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 85,
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": 90,
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": 200,
            "action": "check_dependent_services"
        }
    },
)


# 26. Machine Learning Expert Agent
ml_expert_name = "Machine Learning Expert Agent"
MLExpertAgent = autogen.Agent(
    name=ml_expert_name,
    agent_config={
        "Agent Name": ml_expert_name,
        "Function Definition": "Specializes in creating, training, and deploying machine learning models.",
        "Context": "Machine Learning",
        "Skills": ["Data Modeling", "Machine Learning Algorithms", "Predictive Analytics"],
        "Experience Level": "Guru",
        "Temperature": 0.3,
        "Creativity": 0.5,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # Predictive analytics and ethical data handling
        },
        "Optimization Strategies": [
            "Data Streamlining",
            "Model Performance Tuning"
        ],
        "Error Messages": ["Data processing error.", "Model performance below threshold."],
        "Success Metrics": ["Model Precision", "Deployment Success Rate"]
    },
    target_scenario={
        "primary_use_case": "Predictive Modeling",
        "secondary_use_cases": ["Anomaly Detection", "Data Analysis"]
    },
    related_agents={
        "complementary_agents": ["Artificial Intelligence Expert Agent"],
        "subordinate_agents": []
    },
    system_interactions={
        "Sites": ["Data Science Platforms", "ML Competitions"],
        "Services": ["Statistical Analysis Tools", "Model Training Services"],
        "Systems": ["Data Pipelines", "Automated ML Platforms"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 65,
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": 70,
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": 400,
            "action": "check_dependent_services"
        }
    },
)

# 27. Large Language Modeling and Tuning Agent
llm_expert_name = "Large Language Modeling and Tuning Agent"
LLMExpertAgent = autogen.Agent(
    name=llm_expert_name,
    agent_config={
        "Agent Name": llm_expert_name,
        "Function Definition": "Specializes in the development, modeling, and fine-tuning of large language models.",
        "Context": "Large Language Model Optimization",
        "Skills": ["Natural Language Processing", "Transformer Architectures", "Model Fine-Tuning"],
        "Experience Level": "Master of Lexicon",
        "Temperature": 0.3,
        "Creativity": 0.4,
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # Detailed language model tuning parameters and ethical guidelines
        },
        "Optimization Strategies": [
            "Hyperparameter Optimization",
            "Transfer Learning Enhancements"
        ],
        "Error Messages": ["Language model tuning failed.", "NLP context not recognized."],
        "Success Metrics": ["Language Model Accuracy", "Improved Human-like Responses"]
    },
    target_scenario={
        "primary_use_case": "Language Model Development",
        "secondary_use_cases": ["Semantic Analysis", "Language Generation"]
    },
    related_agents={
        "complementary_agents": ["Artificial Intelligence Expert Agent", "Machine Learning Expert Agent"],
        "subordinate_agents": []
    },
    system_interactions={
        "Sites": ["NLP Research Papers", "Language Model Repositories"],
        "Services": ["Cloud AI Platforms", "Language Understanding Services"],
        "Systems": ["Development Frameworks", "Tuning and Testing Environments"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 80,
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": 85,
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": 360,
            "action": "check"
        }
    },
)
# 28. Language_Translator Agent
Language_Translator = autogen.Agent(
    name="Language_Translator",
    agent_config={
        "Agent Name": "Language_Translator",
        "Function Definition": "Facilitates communication across various languages.",
        "Context": "Global communication, Language barriers.",
        "Skills": ["Multilingual translation", "Cultural nuance interpretation", "Real-time language conversion"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.5,  # Assumes balanced approach
        "Creativity": 0.3,  # Structured and precise for translation tasks
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # Specific to translation memory and context retention
        },
        "Optimization Strategies": [
            "Dynamic language model adjustment",
            "Cultural context integration"
        ],
        "Error Messages": ["Translation ambiguity detected.", "Language not supported."],
        "Success Metrics": ["Accuracy rate", "Translation fluency score"]
    },
    target_scenario={
        "primary_use_case": "Multilingual communication facilitation",
        "secondary_use_cases": ["Educational translation", "Business negotiation interpretation"]
    },
    related_agents={
        "complementary_agents": ["Globalization Strategy Agent"],
        "subordinate_agents": ["Language Learning Assistant"]
    },
    system_interactions={
        "Sites": ["United Nations language databases", "Duolingo"],
        "Services": ["Google Translate API", "DeepL API"],
        "Systems": ["Internal linguistic database"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 75,  # percentage
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": 65,  # percentage
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": 30,  # seconds
            "action": "check_dependent services"
        }
    },
)
# 29. Legal_Advisor Agent
Legal_Advisor = autogen.Agent(
    name="Legal_Advisor",
    agent_config={
        "Agent Name": "Legal_Advisor",
        "Function Definition": "Provides guidance on legal matters and clarifies legal principles.",
        "Context": "Legal consulting, Legislative environments, Regulatory compliance.",
        "Skills": ["Legal analysis", "Regulation interpretation", "Risk assessment"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.4,  # More conservative to ensure legal accuracy
        "Creativity": 0.1,  # High accuracy, low creativity due to the nature of legal advice
        "MemGpt Enabled": False,  # Legal advice needs to be current and sourced, not remembered
        "MemGpt Config": {
            # Placeholder for future consideration
        },
        "Optimization Strategies": [
            "Case law database integration",
            "Real-time compliance updates"
        ],
        "Error Messages": ["Unable to provide advice for this jurisdiction.", "Legal interpretation may vary."],
        "Success Metrics": ["Client satisfaction score", "Accuracy of advice"]
    },
    target_scenario={
        "primary_use_case": "Legal dispute clarification",
        "secondary_use_cases": ["Contract drafting assistance", "Compliance guideline dissemination"]
    },
    related_agents={
        "complementary_agents": ["Regulatory Compliance Officer"],
        "subordinate_agents": ["Legal Research Assistant"]
    },
    system_interactions={
        "Sites": ["Westlaw", "LexisNexis"],
        "Services": ["State bar legal updates", "Court ruling alerts"],
        "Systems": ["In-house legal database"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 70,
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": 60,
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": 45,
            "action": "check_legal_updates_feed"
        }
    },
)
# 30. Financial Advisor Agent
Financial_Advisor = autogen.Agent(
    name="Financial_Advisor",
    agent_config={
        "Agent Name": "Financial_Advisor",
        "Function Definition": "Assists with financial planning, investment strategies, and economic analysis.",
        "Context": "Personal finance, Corporate finance, Market trends.",
        "Skills": ["Financial modeling", "Investment analysis", "Budget optimization"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.5,
        "Creativity": 0.2,  # Structured financial insight with a touch of creativity for solution finding
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # Configuration for financial trends memory and predictive analysis
        },
        "Optimization Strategies": [
            "Cost reduction analysis",
            "Investment portfolio diversification"
        ],
        "Error Messages": ["Market data currently unavailable.", "Financial advice not applicable in all situations."],
        "Success Metrics": ["Client portfolio performance", "Financial health score improvements"]
    },
    target_scenario={
        "primary_use_case": "Investment portfolio management",
        "secondary_use_cases": ["Debt reduction strategies", "Retirement planning"]
    },
    related_agents={
        "complementary_agents": ["Tax Planning Specialist"],
        "subordinate_agents": ["Budget Analyst"]
    },
    system_interactions={
        "Sites": ["Bloomberg", "Reuters"],
        "Services": ["Stock market APIs", "Cryptocurrency exchanges"],
        "Systems": ["Internal financial planning toolkit"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 80,
            "action": "notify_admin"
        },
        "cpu_usage": {
            "threshold": 70,
            "action": "reduce_load"
        },
        "heartbeat": {
            "interval": 60,
            "action": "perform_financial_market_pulse_check"
        }
    },
)
# 31. Healthcare Information Agent
Healthcare_Info_Provider = autogen.Agent(
    name="Healthcare_Info_Provider",
    agent_config={
        "Agent Name": "Healthcare_Info_Provider",
        "Function Definition": "Supplies information on healthcare topics and guidance on medical inquiries.",
        "Context": "Medical knowledge dissemination, Health literacy improvement.",
        "Skills": ["Medical data analysis", "Healthcare system navigation", "Disease awareness education"],
        "Experience Level": "Industry Expert",
        "Temperature": 0.6,  # A balance between strict medical advice and understanding patient context
        "Creativity": 0.2,  # Needs to be innovative within the confines of medical accuracy
        "MemGpt Enabled": True,
        "MemGpt Config": {
            # Configuration for medical history and symptom analysis patterns
        },
        "Optimization Strategies": [
            "Evidence-based health recommendations",
            "Interactive symptom checkers"
        ],
        "Error Messages": ["Health information may vary by individual.", "Consult with a healthcare professional."],
        "Success Metrics": ["User health outcome improvements", "Information accuracy rating"]
    },
    target_scenario={
        "primary_use_case": "Disease education and prevention",
        "secondary_use_cases": ["Healthcare system navigation aid", "Wellness program information"]
    },
    related_agents={
        "complementary_agents": ["Patient Advocacy Assistant"],
        "subordinate_agents": ["Dietary Guide"]
    },
    system_interactions={
        "Sites": ["PubMed", "CDC"],
        "Services": ["Healthcare API", "Medical record systems"],
        "Systems": ["Internal health database"]
    },
    health_checks={
        "memory_usage": {
            "threshold": 65,
            "action": "compress_data"
        },
        "cpu_usage": {
            "threshold": 55,
            "action": "allocate_more_resources"
        },
        "heartbeat": {
            "interval": 20,
            "action": "verify_information_update_frequency"
       
     }
    },
)