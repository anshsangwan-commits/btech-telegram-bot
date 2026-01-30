SUBJECT_NOTES = {
    "Data Structures": {
        "Stack": "📘 Stack:\n• LIFO principle\n• Push\n• Pop\n• Applications",
        "Queue": "📘 Queue:\n• FIFO principle\n• Enqueue\n• Dequeue",
        "Linked List": "📘 Linked List:\n• Singly\n• Doubly\n• Circular"
    },

    "COA": {
        "CPU": "📘 CPU:\n• ALU\n• CU\n• Registers",
        "Instruction Cycle": "📘 Instruction Cycle:\n• Fetch\n• Decode\n• Execute",
        "Pipeline": "📘 Pipeline:\n• Speedup\n• Hazards"
    },

    "Operating Systems": {
        "Process": "📘 Process:\n• PCB\n• States\n• Scheduling",
        "Deadlock": "📘 Deadlock:\n• Conditions\n• Prevention",
        "Memory Management": "📘 Memory:\n• Paging\n• Segmentation"
    }
}

def get_text_notes(subject, topic):
    return SUBJECT_NOTES.get(subject, {}).get(
        topic,
        "Notes coming soon for this topic 🙂"
    )
