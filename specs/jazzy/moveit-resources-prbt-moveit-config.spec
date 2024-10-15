# Meta Package
Name:           ros-jazzy-moveit-resources-prbt-moveit-config
Version:        2.10.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_resources_prbt_moveit_config and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_resources_prbt_moveit_config
Requires:       ros2-jazzy-moveit_resources_prbt_moveit_config-devel

Obsoletes: ros-jazzy-moveit-resources-prbt-moveit-config < 2.10.0-1

%description
ROS jazzy package moveit_resources_prbt_moveit_config.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
