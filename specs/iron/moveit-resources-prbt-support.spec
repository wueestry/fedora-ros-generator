# Meta Package
Name:           ros-iron-moveit-resources-prbt-support
Version:        2.8.0
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-iron-moveit_resources_prbt_support and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_resources_prbt_support
Requires:       ros2-iron-moveit_resources_prbt_support-devel

Obsoletes: ros-iron-moveit-resources-prbt-support < 2.8.0-1

%description
Mechanical, kinematic and visual description of the Pilz light weight
arm PRBT.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
