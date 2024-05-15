



const MainContent = () => {
    return (
    <>
    <div className="hbox full">
        <div className="vbox third">
            <h1>Portfolio</h1>
            <h2 className="clickable" href="https://www.google.com/search?q=projects">Projects</h2>
            <ul>
                <li className="clickable" href="https://www.google.com/search?q=project1">Project 1</li>
                <li className="clickable" href="https://www.google.com/search?q=project2">Project 2</li>
                <li className="clickable" href="https://www.google.com/search?q=project3">Project 3</li>
            </ul>
        </div>

        <div className="vbox third clickable" href="https://www.google.com/search?q=about+me">
            <h2>About Me</h2>
            <p>My name is John Doe and I am a web developer.</p>
        </div>

        <div className="vbox third clickable" href="https://www.google.com/search?q=contact">
            <h2>Contact</h2>
            <p>Email:
                <a href="mailto:linus@linus-minus-sinus.org" target="_blank">linus@linus-minus-sinus.org</a>
            </p>
        </div>
    </div>

    <div className="hbox full">
        <div className="vbox half">
            <h2 className="clickable" href="https://www.google.com/search?q=skills">Skills</h2>
            <ul>
                <li className="clickable" href="https://www.google.com/search?q=html">HTML</li>
                <li className="clickable" href="https://www.google.com/search?q=css">CSS</li>
                <li className="clickable" href="https://www.google.com/search?q=javascript">JavaScript</li>
                <li className="clickable" href="https://www.google.com/search?q=react">React</li>
            </ul>
        </div>

        <div className="vbox half clickable" href="https://www.google.com/search?q=experience">
            <h2>Experience</h2>
            <p>Web Developer at Company X</p>
        </div>
    </div>

        <div className="hbox full">
            <div className="vbox full clickable" href="https://www.google.com/search?q=education">
                <h2>Education</h2>
                <p>University of Web Development</p>
            </div>
        </div>

        <div className="vbox full">
            <h2 className="clickable" href="https://www.google.com/search?q=projects">Projects</h2>
            <div className="hbox full">
                <div className="vbox half clickable" href="https://www.google.com/search?q=project1">
                    <h3>Project 1</h3>
                <   p>Project 1 description</p>
                </div>
            <div className="vbox half clickable" href="https://www.google.com/search?q=project2">
                <h3>Project 2</h3>
                <p>Project 2 description</p>
            </div>
            <div className="vbox half clickable" href="https://www.google.com/search?q=project3">
                <h3>Project 3</h3>
                <p>Project 3 description</p>
            </div>
        </div>
    </div>
    </>
    );
}

export default MainContent;