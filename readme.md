1.Why lists are used instead of variables?

- Variables store a single value (e.g., x = 10).
- Lists store multiple values in one place (e.g., numbers = [10, 20, 30]).
- Benefits of lists:
- ✅ Compact storage: Instead of creating x1, x2, x3, you can store all values in one list.
- ✅ Iteration: You can loop through a list easily.
- ✅ Dynamic: Lists can grow or shrink at runtime.
- ✅ Flexibility: They can hold mixed data types ([10, "AI", True]).

2.Difference between list and string
 A string is essentially a specialized list of characters, but it’s restricted and immutable.
- Lists ≠ strings because lists are mutable & multi-type, strings are immutable & text-only.

3.How lists relate to ML datasets?
- In Machine Learning, datasets are collections of values (numbers, text, labels).
- Lists are often the first step in representing data:
- Example: features = [5.1, 3.5, 1.4, 0.2] (iris flower measurements).
- Example: labels = ["spam", "ham", "spam"] (text classification).
- Later, lists are converted into NumPy arrays or Pandas DataFrames for efficiency:
- Lists → Arrays → Matrices → Datasets
- Think of lists as the raw container for data before it’s structured into ML-ready formats.

