# Meta Package
Name:           ros-iron-moveit-resources-panda-moveit-config
Version:        2.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org/
Summary:        Meta package for ros2-iron-moveit_resources_panda_moveit_config and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_resources_panda_moveit_config
Requires:       ros2-iron-moveit_resources_panda_moveit_config-devel

Obsoletes: ros-iron-moveit-resources-panda-moveit-config < 2.1.1-1

%description
ROS iron package moveit_resources_panda_moveit_config.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.1.1-1
- Update to latest release
