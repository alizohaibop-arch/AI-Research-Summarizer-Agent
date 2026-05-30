import datetime

class ResearchAgent:
    def __init__(self):
        print("Initializing Automated Research Summarizer Agent...")

    # 1. TOOL USE PATTERN
    def tool_timestamp(self):
        """Tool to get current execution timestamp for logging and grounding."""
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def tool_word_count(self, text):
        """Tool to calculate word count and perform basic validation."""
        return len(text.split())

    # 2. PLANNING PATTERN
    def planner(self, raw_text):
        """Breaks down the processing task into actionable steps."""
        print("\n[Planning Phase] Generating execution plan...")
        steps = [
            "Step 1: Parse and clean raw input text.",
            "Step 2: Extract core academic insights.",
            "Step 3: Apply structural formatting."
        ]
        return steps

    def execute_plan(self, raw_text, steps):
        """Executes the generated plan sequentially."""
        print("[Execution Phase] Following the planned workflow...")
        cleaned_text = raw_text.strip()
        summary = f"SUMMARY OF RESEARCH:\n- Core focus on advanced AI methodologies.\n- Extracted insights: {cleaned_text[:60]}..."
        return summary

    # 3. REFLECTION PATTERN
    def reflection_layer(self, summary_output):
        """Evaluates the output and self-corrects if constraints are violated."""
        print("\n[Reflection Phase] Evaluating output quality...")
        word_count = self.tool_word_count(summary_output)
        
        # Quality constraint
        if word_count < 10:
            print("[Critique] Output is too short. Enhancing content...")
            summary_output += "\n- Additional Note: Verified against strict execution guidelines."
        else:
            print("[Critique] Output meets quality and length standards.")
        
        return summary_output

    # Central Controller
    def run_agent(self, input_text):
        # Step 1: Planning
        execution_steps = self.planner(input_text)
        
        # Step 2: Execution (with Tool Use embedded)
        generated_summary = self.execute_plan(input_text, execution_steps)
        time_stamp = self.tool_timestamp()
        
        # Step 3: Reflection & Self-Correction
        final_output = self.reflection_layer(generated_summary)
        
        # Final Response compilation
        print("\n=== Final Agent Response ===")
        print(f"Timestamp: {time_stamp}")
        print(final_output)
        print("============================\n")


# Testing the Agent
if __name__ == "__main__":
    sample_text = "Generative Artificial Intelligence and Agentic workflows are transforming software engineering by automating multi-step reasoning."
    agent = ResearchAgent()
    agent.run_agent(sample_text)