import {render, screen} from "@testing-library/react";
import Greet from "./Greet";

describe("Greet Form", () => {
    test("renders correctly" ,() =>{
        render(<Greet />);
        const nameElement = screen.getByRole("textbox");
        expect(nameElement).toBeInTheDocument();

    });
});