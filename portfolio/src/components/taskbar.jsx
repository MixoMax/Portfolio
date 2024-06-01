

import {useState, useEffect} from 'react';

const Taskbar = ({ children }) => {

    const [maximized_arr, setMaximizedArr] = useState(Array(children.length).fill(false));
    const [minimized_arr, setMinimizedArr] = useState(Array(children.length).fill(false));

    return (
        <div className="taskbar">
            {children.map((child, index) => {
                return (
                    <div className="task" key={index}>
                        {child.props.title}
                    </div>
                );
            })}
        </div>
    );
}

export default Taskbar;