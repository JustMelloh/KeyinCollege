import { render, screen } from "@testing-library/react";
import Greet from "./Greet";

describe("Greet Form", () => {
  test("renders correctly", () => {
    render(<Greet />);

    const nameELement1 = screen.getByRole("textbox", { name: "name" });
    expect(nameELement1).toBeInTheDocument();

    const nameElement2 = screen.getByRole("textbox", { name: "Comment" });
    expect(nameElement2).toBeInTheDocument();

    const comboElement = screen.getByRole("combobox");
    expect(comboElement).toBeInTheDocument();

    const checkBoxElement = screen.getByRole("checkbox");
    expect(checkBoxElement).toBeInTheDocument();

    const pageHeading = screen.getByRole("heading", {level: 1});
    expect(pageHeading).toBeInTheDocument();

    const pageHeading2 = screen.getByRole("heading", {level: 2});
    expect(pageHeading2).toBeInTheDocument();

    const nameElement3 = screen.getByLabelText("Location");
    expect(nameElement3).toBeInTheDocument();

    const lblElement = screen.getByLabelText("I agree");
    expect(lblElement).toBeInTheDocument();


    const plcElement = screen.getByPlaceholderText("Enter your name here");
    expect(plcElement).toBeInTheDocument();

    const nameElement4 = screen.getByDisplayValue("keyin");
    expect(nameElement4).toBeInTheDocument();

    const paraElement = screen.getByTestId("p1");
    expect(paraElement).toBeInTheDocument();

    
  });
});
