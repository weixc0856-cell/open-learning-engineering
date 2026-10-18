/* Small, dependency-free self-check interactions for the course pages. */
document.addEventListener("click", (event) => {
  const button = event.target.closest(".quiz-submit");
  if (!button) return;
  const quiz = button.closest("[data-quiz]");
  if (!quiz) return;

  const answers = { q1: "b", q2: "b" };
  let correct = 0;
  let answered = 0;
  Object.entries(answers).forEach(([name, answer]) => {
    const selected = quiz.querySelector(`input[name="${name}"]:checked`);
    const feedback = quiz.querySelector(`[data-feedback="${name}"]`);
    if (selected) {
      answered += 1;
      if (selected.value === answer) correct += 1;
    }
    if (feedback) feedback.hidden = !selected || selected.value !== answer;
  });

  const result = quiz.querySelector(".quiz-result");
  if (result) {
    result.textContent = answered < Object.keys(answers).length
      ? `已回答 ${answered}/2 题。请完成所有题目后再检查。`
      : `得分：${correct}/2。${correct === 2 ? "全部正确，继续动手验证。" : "展开对应解释，回到正文核对概念后再试一次。"}`;
  }
});
