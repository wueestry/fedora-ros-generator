# Meta Package
Name:           ros-humble-image-proc
Version:        3.0.5
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/image_proc/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-humble-image_proc and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-image_proc
Requires:       ros2-humble-image_proc-devel

Obsoletes: ros-humble-image-proc < 3.0.5-1

%description
Single image rectification and color processing.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.5-1
- Update to latest release
