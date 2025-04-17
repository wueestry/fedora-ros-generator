# Meta Package
Name:           ros-jazzy-moveit-resources-prbt-ikfast-manipulator-plugin
Version:        2.10.0
Release:        2%{?dist}
License:        Apache 2.0
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_resources_prbt_ikfast_manipulator_plugin and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_resources_prbt_ikfast_manipulator_plugin
Requires:       ros2-jazzy-moveit_resources_prbt_ikfast_manipulator_plugin-devel

Obsoletes: ros-jazzy-moveit-resources-prbt-ikfast-manipulator-plugin < 2.10.0-2

%description
The prbt_ikfast_manipulator_plugin package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Nov 21 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-2
- Rebuild due to srdfdom update
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
