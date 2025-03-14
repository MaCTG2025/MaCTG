import re

str_test = [
    "```python\n",
    "import numpy as np\n",
    "```\n",
    "```python\n",
    "def extract_blue_channel(image_data: np.ndarray) -> np.ndarray:\n",
    "    \"\"\"\n",
    "    Extract the Blue channel from the input RGB image data,\n",
    "    setting the Red and Green channels to zero.\n",
    "    \"\"\"\n",
    "    if image_data.shape[2] != 3:\n",
    "        raise ValueError(\"The input image_data must have a shape of (height, width, 3)\")\n",
    "\n",
    "    # Set Red and Green channels to zero\n",
    "    image_data[:, :, 0] = 0\n",
    "\n",
    "    return image_data[:, :, 2]\n",
    "```\n",
    "Here is the code for the function you have implemented:\n",
]

# extarct function code inside the code block
code = ""
function_code = re.findall(r"```(.*?)```", "".join(str_test), re.DOTALL)
for i in function_code:
    # sometimes the code starts with ```python, remove it
    if i.startswith("python"):
        i = i[6:]
    code += i

print(code)