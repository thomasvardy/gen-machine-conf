#!/usr/bin/env python3

# Copyright (C) 2023, Advanced Micro Devices, Inc.  All rights reserved.
#
# Author:
#       Raju Kumar Pothuraju <rajukumar.pothuraju@amd.com>
#
# SPDX-License-Identifier: MIT


import os
import common_utils
import project_config
import logging
import glob
import pathlib

logger = logging.getLogger('Gen-Machineconf')

class CreateMultiConfigFiles():
    def ParseCpuDict(self):
        # Return list of conf files if files_only True
        if self.ReturnConfFiles:
            return self.MultiConfFiles, self.MultiConfMin
        # MultiConfDict will have the configuration info
        # to create machine and local.conf files
        return self.MultiConfDict

    def __init__(self, args, cpu_info_dict, system_conffile='', file_names_only=False):
        self.MultiConfFiles = []
        self.MultiConfMin = []
        self.MultiConfUser = []
        self.MultiConfDict = {}
        self.cpu_info_dict = cpu_info_dict
        self.args = args

        # self.ReturnConfFiles if true returns the file names which is required
        # to create Kconfig
        self.ReturnConfFiles = file_names_only
        if system_conffile:
            # Get the BBMC targets from system config file and generate
            # multiconfig targets only for enabled
            self.MultiConfUser = common_utils.GetConfigValue(
                                        'CONFIG_YOCTO_BBMC_', system_conffile,
                                        'choicelist', '=y').lower().replace('_', '-')
            self.MultiConfUser = list(self.MultiConfUser.split(' '))
