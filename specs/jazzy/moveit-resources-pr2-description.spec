# Meta Package
Name:           ros-jazzy-moveit-resources-pr2-description
Version:        3.0.0
Release:        2%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_resources_pr2_description and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_resources_pr2_description
Requires:       ros2-jazzy-moveit_resources_pr2_description-devel

Obsoletes: ros-jazzy-moveit-resources-pr2-description < 3.0.0-2

%description
PR2 Resources used for MoveIt! testing

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Nov 21 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.0.0-2
- Rebuild due to srdfdom update
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.0.0-1
- Update to latest release
