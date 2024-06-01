// cragable tag to surrond the component to make it dragable

import { useEffect, useState } from "react";

const Dragable = ({ children, title}) => {
    const [dragging, setDragging] = useState(false);
    const [pos, setPos] = useState({ x: Math.random() * 400, y: Math.random() * 400 });
    const [release_pos, setReleasePos] = useState({ x: 0, y: 0 });

    useEffect(() => {
        if (!dragging) {
            setReleasePos({ x: pos.x, y: pos.y });
        }
    
        const onMouseMove = (e) => {
            if (dragging) {
                var delta_x = release_pos.x - e.clientX;
                var delta_y = release_pos.y - e.clientY;
                setPos({ x: pos.x - delta_x, y: pos.y - delta_y });
            }
        };

        const onMouseUp = () => {
            setDragging(false);
        };

        document.addEventListener("mousemove", onMouseMove);
        document.addEventListener("mouseup", onMouseUp);

        return () => {
            document.removeEventListener("mousemove", onMouseMove);
            document.removeEventListener("mouseup", onMouseUp);
        };
    }, [dragging]);


    return (
        <div
            style={{
                position: "absolute",
                left: pos.x,
                top: pos.y,
                cursor: dragging ? "grabbing" : "grab",
            }}
            onMouseDown={() => setDragging(true)}
        >

        {children}
        </div>
    );
}

export default Dragable;