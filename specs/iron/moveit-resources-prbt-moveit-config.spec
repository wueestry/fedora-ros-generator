# Meta Package
Name:           ros-iron-moveit-resources-prbt-moveit-config
Version:        2.8.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-iron-moveit_resources_prbt_moveit_config and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_resources_prbt_moveit_config
Requires:       ros2-iron-moveit_resources_prbt_moveit_config-devel

Obsoletes: ros-iron-moveit-resources-prbt-moveit-config < 2.8.0-1

%description
ROS iron package moveit_resources_prbt_moveit_config.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
