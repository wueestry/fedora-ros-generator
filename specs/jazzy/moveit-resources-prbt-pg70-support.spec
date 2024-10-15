# Meta Package
Name:           ros-jazzy-moveit-resources-prbt-pg70-support
Version:        2.10.0
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_resources_prbt_pg70_support and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_resources_prbt_pg70_support
Requires:       ros2-jazzy-moveit_resources_prbt_pg70_support-devel

Obsoletes: ros-jazzy-moveit-resources-prbt-pg70-support < 2.10.0-1

%description
PRBT support for Schunk pg70 gripper.

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
