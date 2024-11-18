from mygame import main
from mygame.utils import frozen

if __name__ == "__main__":
    frozen.fix_cwd_for_frozen_execution()

    main()
