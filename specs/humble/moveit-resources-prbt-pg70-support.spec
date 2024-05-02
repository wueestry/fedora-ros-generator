# Meta Package
Name:           ros-humble-moveit-resources-prbt-pg70-support
Version:        2.5.5
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-humble-moveit_resources_prbt_pg70_support and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-moveit_resources_prbt_pg70_support
Requires:       ros2-humble-moveit_resources_prbt_pg70_support-devel

Obsoletes: ros-humble-moveit-resources-prbt-pg70-support < 2.5.5-1

%description
PRBT support for Schunk pg70 gripper.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.5-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.4-1
- Initial humble build
