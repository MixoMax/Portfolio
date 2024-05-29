import { useState, useEffect } from 'react';

const Cmd = () => {

    var cmd = "neofetch";
    var neofetch_output = {
        "user": "linus@linus-minus-sinus.org",
        
        "location": "Hamburg, Germany",
        "geo": "53.55, 10.00",

        "education": [
            {
                "degree": "Bachelor of Science",
                "major": "Computer Science",
                "school": "University of Hamburg",
                "graduation": "2021"
            }
        ],
        "work": [
            {
                "position": "Software Engineer",
                "company": "Google",
                "years": "2021 - Present"
            }
        ],
        "languages": [
            {
                "name": "German",
                "proficiency": "Native"
            },
            {
                "name": "English",
                "proficiency": "Fluent"
            }
        ],
        "programming_languages": [
            // Python, JS, React, SQLite, HTML+css
            {
                "name": "Python",
                "proficiency": "Advanced"
            },
            {
                "name": "JavaScript",
                "proficiency": "Advanced"
            },
            {
                "name": "React",
                "proficiency": "Advanced"
            },
            {
                "name": "SQLite",
                "proficiency": "Advanced"
            },
            {
                "name": "HTML",
                "proficiency": "Advanced"
            },
            {
                "name": "CSS",
                "proficiency": "Advanced"
            }
        ],

        "tools": [
            // Git, Docker, VSCode, Linux
            {
                "-": "Git",
            },
            {
                "-": "Docker",
            },
            {
                "-": "VSCode",
            },
            {
                "-": "Linux",
            }
        ],

        "interests": [
            "Machine Learning",
            "Web Development",
            "Open Source",
            "Linux",
            "Cryptography"
        ],
    };

    var neofetch_output_str = ""
    for (var key in neofetch_output) {
        var value = neofetch_output[key];
        if (!Array.isArray(value)) {
            neofetch_output_str += key + ": " + value + "\n";
        } else {
            neofetch_output_str += "=".repeat(key.length) + "\n";
            neofetch_output_str += key + ":\n";
            
            // if array of strings
            if (typeof value[0] === "string") {
                for (var i = 0; i < value.length; i++) {
                    neofetch_output_str += value[i] + "\n";
                }
            } else {
                for (var i = 0; i < value.length; i++) {
                    var obj = value[i];
                    for (var k in obj) {
                        neofetch_output_str += k + ": " + obj[k] + "\n";
                    }
                    
                    if (i < value.length - 1) {
                        neofetch_output_str += "\n";
                    }
                }
            }

            neofetch_output_str += "=".repeat(key.length) + "\n";
            neofetch_output_str += "\n";
        }
    }

    const [output, setOutput] = useState("");
    const [ticks, setTicks] = useState(0);

    useEffect(() => {
        setTimeout(() => {
            var new_ticks = ticks + 1;
            new_ticks = new_ticks % (neofetch_output_str.length + 1);
            setTicks(new_ticks);
        }, 1);

    }, [ticks]);

    useEffect(() => {
        var output = cmd + "\n";

        if (ticks < neofetch_output_str.length) {
            output += neofetch_output_str.substring(0, ticks);
        } else {
            output += neofetch_output_str;
        }


        // replace all newlines with <br>
        output = output.replace(/\n/g, "<br>");


        setOutput(output);

    }, [ticks]);
    

    return (
        <div className="cmd">
            <div className="cmd__output" dangerouslySetInnerHTML={{__html: output}}></div>
        </div>
    );
}

export default Cmd;