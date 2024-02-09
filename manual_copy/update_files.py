import vllm, os 
import shutil

path = os.path.dirname(vllm.__file__)

to_copy = [
    "../vllm/model_executor/layers/sampler.py",
    "../vllm/outputs.py",
    "../vllm/sampling_params.py",
    "../vllm/sequence.py",
]

if vllm.__version__ != "0.3.0":
    raise Exception("This copy and replace method is only applicable to vLLM v0.3.0!!")

for _dir in to_copy:
    print(_dir, os.path.join(path, _dir.replace("../vllm/", "")))
    try:
        shutil.copyfile(_dir, os.path.join(path, _dir.replace("../vllm/", "")))
    except shutil.SameFileError:
        print("Skipped")
print("DONE.")